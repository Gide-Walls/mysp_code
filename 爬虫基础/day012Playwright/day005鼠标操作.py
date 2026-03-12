from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(r'D:\图灵课程学习\爬虫基础\day012Playwright\练习鼠标操作.html')
    # 获取红色方块源的位置
    red_dex = page.locator('#red-box')
    red_box_box = red_dex.bounding_box()  # 获取元素的坐标大小

    # 获取绿色源的位置
    green_dex = page.locator('#green-box')
    green_box_box = green_dex.bounding_box()

    if red_box_box and green_box_box:
        # 计算红色块中心的位置
        from_x = red_box_box["x"] + red_box_box["width"] / 2
        from_y = red_box_box["y"] + red_box_box["height"] / 2

        # 计算绿色的中心位置
        to_x = green_box_box["x"] + green_box_box["width"] / 2
        to_y = green_box_box["y"] + green_box_box["height"] / 2

        page.mouse.move(x=from_x, y=from_y)
        page.mouse.down()
        page.wait_for_timeout(10000)
        # 移动到目标位置
        page.mouse.move(x=to_x, y=to_y)
        # 释放鼠标
        page.mouse.up()
        print('移动完成')

    input()
    browser.close()

    # # 移动鼠标
    # page.mouse.move(x=94, y=100)
    # # 点击鼠标
    # page.mouse.down()
    #
    # # 移动到特定位置
    # page.mouse.move(x=309, y=151)
    #
    # # 释放鼠标
    # page.mouse.move(x=500, y=300)
    # page.mouse.up()
    # # page.wait_for_timeout(100000)

    input()
