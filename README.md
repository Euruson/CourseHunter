# CourseHunter

自动化抢课脚本：现只针对UESTC，有兴趣的同学可以添加其他学校的相应抢课程序。

## selenium以及chromedriver

UESTC.py主要使用selenium模块来模拟浏览器操作，需要下载chrome浏览器的[chromedriver接口](https://chromedriver.chromium.org/), 请在上面网站中根据浏览器版本，下载相应版本的chromedriver。

## 配置

在`def __init__(self, driver_path: str = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")`将地址更换为你的chromedriver所在位置。

在`option.add_argument(r"user-data-dir=C:\Users\yulin\AppData\Local\Google\Chrome\User Data")` 中将地址更换为chrome用户数据所在位置（以便使用cookie免登陆进行抢课）。

在`xk.selectCourse(course_nums=["0808126006", "0808126007"])`中将`course_nums`更换为需要抢课的课程编号。

## Gotcha

需要先登陆至学校抢课页面，并且关闭浏览器后启动本程序。