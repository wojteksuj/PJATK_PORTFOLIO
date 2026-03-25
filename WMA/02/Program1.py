import cv2 as cv

def imshow(title, image):
    cv.imshow(title,image)
    k = cv.waitKey(0)#0 infinity waiting time
    if k == ord("s"):
        cv.imwrite(f"00_{title}_saved.jpg", image)
    cv.destroyAllWindows()
    return

img = cv.imread("assets/tray8.jpg")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(imgray, 127, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# tray = largest contour
tray = max(contours, key=cv.contourArea)

# area
area = cv.contourArea(tray)
print("Tray area:", area)

# draw tray
cv.drawContours(img, [tray], -1 , (0,255,0), 2)

imshow("tray", img)