import cv2
import mediapipe as mp
import numpy as np
import time

# ==========================
# INITIALIZATION
# ==========================
cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)

board = [""] * 9
current_player = "X"
game_over = False
menu_active = True

selected_cell = None
hover_start = 0
HOVER_TIME = 1.2
gesture_cooldown = 0

winning_cells = None

# ==========================
# UI FUNCTIONS
# ==========================
def draw_grid(img):
    h, w, _ = img.shape
    for i in range(1, 3):
        cv2.line(img, (0, h*i//3), (w, h*i//3), (255,255,255), 2)
        cv2.line(img, (w*i//3, 0), (w*i//3, h), (255,255,255), 2)

def draw_marks(img):
    h, w, _ = img.shape
    for i in range(9):
        if board[i]:
            x = (i % 3) * w // 3 + w // 6
            y = (i // 3) * h // 3 + h // 6
            cv2.putText(img, board[i], (x-30, y+30),
                        cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 5)

def draw_menu(img):
    cv2.rectangle(img, (150,150), (500,400), (0,0,0), -1)
    cv2.putText(img, "GESTURE MENU", (190,190),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.putText(img, "START GAME", (220,250),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.putText(img, "RESET GAME", (220,300),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.putText(img, "EXIT", (220,350),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

def draw_winning_line(img):
    if not winning_cells:
        return
    h, w, _ = img.shape
    a,b,c = winning_cells
    def center(i):
        return ((i % 3) * w // 3 + w//6,
                (i // 3) * h // 3 + h//6)
    cv2.line(img, center(a), center(c), (0,0,255), 10)

# ==========================
# GAME LOGIC
# ==========================
def check_winner():
    global winning_cells
    combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in combos:
        if board[a] == board[b] == board[c] != "":
            winning_cells = (a,b,c)
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def reset_game():
    global board, game_over, current_player, winning_cells
    board = [""] * 9
    current_player = "X"
    game_over = False
    winning_cells = None

def get_cell(x,y,w,h):
    if x<0 or y<0 or x>w or y>h:
        return None
    col = x // (w//3)
    row = y // (h//3)
    cell = int(row*3 + col)
    return cell if 0<=cell<=8 else None

# ==========================
# GESTURE DETECTION
# ==========================
def is_open_palm(lm):
    tips = [8,12,16,20]
    count = 0
    for t in tips:
        if lm[t].y < lm[t-2].y:
            count += 1
    return count == 4

def is_fist(lm):
    return lm[8].y > lm[6].y and lm[12].y > lm[10].y

# ==========================
# MAIN LOOP
# ==========================
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if menu_active:
        draw_menu(img)

    if result.multi_hand_landmarks:
        for i, hand in enumerate(result.multi_hand_landmarks):
            lm = hand.landmark
            ix, iy = int(lm[8].x*w), int(lm[8].y*h)
            cv2.circle(img, (ix,iy), 8, (255,0,0), -1)

            # MENU CONTROL
            if menu_active:
                if 220 < ix < 450:
                    if 230 < iy < 260:
                        menu_active = False
                        reset_game()
                    elif 280 < iy < 310:
                        reset_game()
                    elif 330 < iy < 360:
                        cap.release()
                        cv2.destroyAllWindows()
                        exit()

            # GAME CONTROL
            else:
                if is_open_palm(lm):
                    reset_game()
                    menu_active = True

                handed = result.multi_handedness[i].classification[0].label
                player = "X" if handed == "Left" else "O"

                if player == current_player and not game_over:
                    cell = get_cell(ix,iy,w,h)
                    if cell is not None and board[cell]=="":
                        if selected_cell != cell:
                            selected_cell = cell
                            hover_start = time.time()
                        elif time.time() - hover_start > HOVER_TIME:
                            board[cell] = current_player
                            current_player = "O" if current_player=="X" else "X"
                            selected_cell = None

    if not menu_active:
        draw_grid(img)
        draw_marks(img)

    winner = check_winner()
    if winner:
        game_over = True
        draw_winning_line(img)
        cv2.putText(img, "DRAW!" if winner=="Draw" else f"{winner} WINS!",
                    (180,80), cv2.FONT_HERSHEY_SIMPLEX,
                    1.5, (0,0,255), 4)

    cv2.putText(img, f"Turn: {current_player}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)

    cv2.imshow("Gesture Tic Tac Toe", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
