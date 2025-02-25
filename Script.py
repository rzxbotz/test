class script(object):
    START_MSG = """<b>Welcome to the Calicut University Study Material Bot.</b>

Here, you can easily access <b>study notes</b> and <b>previous year question papers</b> for your courses.  

<i>Select your course using the buttons below to get started.</i>"""
    
    ABOUT_TXT= """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Creator:</b> <a href="https://t.me/Source_Codez/3">This Person</a>  
<b>Language:</b> Python 3  
<b>Library:</b> Pyrogram  
<b>Server:</b> <a href="https://t.me/Source_Codez/3">VPS</a>  
<b>Database:</b> <a href="https://www.mongodb.com/">MongoDB Free Tier</a>  
<b>Build Status:</b> v3.1 [Stable]  

<b><i>@ExamWalletBot</i></b>"""
    
    ABOUT = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<i>Exam Wallet - Your Ultimate Study Companion

Exam Wallet is a user-friendly Telegram bot designed to help Calicut University students easily access study materials.

We provide previous year question papers and study notes, ensuring that students can find everything they need in one place without any hassle. Our goal is to simplify learning by offering well-organized materials that are easy to navigate.

Why choose Exam Wallet? It is simple to use, free from ads and distractions, and focuses entirely on providing quality study resources. With a clean and efficient interface, students can quickly find and access the materials they need.

Start using Exam Wallet today and make studying smarter, not harder.

Happy Learning!</i>

<b><i>@ExamWalletBot</i></b>"""
    
    CREDIT = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<i>The study materials provided in this bot are sourced from various contributors, and academic resources. We appreciate their efforts in making learning accessible to all.</i>

<b><a href="https://t.me/JurazCommerce">Juraz Commerce</a>

<a href="https://t.me/educational_corner">Educational Corner</a></b>

<b><i>@ExamWalletBot</i></b>"""

    COURSE = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Please choose your course from the options below.</b>

<b><i>@ExamWalletBot</i></b>"""

    BCOM = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>You have selected:</b> BCOM

<b><i>@ExamWalletBot</i></b>"""

    MATERIALS2019 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Course Selected:</b> BCOM

Here, you can find <b>study notes</b> and <b>previous year question papers</b> for your course.  

Click the button below to continue.

<b><i>@ExamWalletBot</i></b>"""

    BCM2019SNSEMESTERS = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Course:</b> BCOM  

Now, choose your semester to access the available study materials.

<b><i>@ExamWalletBot</i></b>"""

    BCMSNSEM1 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> First  

Study materials will be <b>added soon.</b>  

<i>Click on the subject name to view available resources.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCMSNSEM2 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> Second  

Study materials will be <b>added soon.</b>  

<i>Click on the subject name to view available resources.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCMSNSEM3 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> Third  

Study materials will be <b>added soon.</b>  

<i>Click on the subject name to view available resources.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCMSNSEM4 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> Fourth  

Study materials will be <b>added soon.</b>  

<i>Click on the subject name to view available resources.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCMSNSEM5 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> Fifth  

Study materials will be <b>added soon.</b>  

<i>Click on the subject name to view available resources.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCMSNSEM6 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> Sixth  

<b><a href=https://t.me/ExamWalletBot?start=Z2V0LTI5OTY3MDIyMDUzMjM1OC0zMDc2ODgxNTI4NTQyOTQ>FINANCIAL DERIVATIVES</a></b>

<b><a href=https://t.me/ExamWalletBot?start=Z2V0LTMxNDcwMzg0MzYzNTk4OC0zMjA3MTcyOTI4Nzc0NDA>AUDITING AND CORPORATE GOVERNANCE</a></b>

<b><a href=https://t.me/ExamWalletBot?start=Z2V0LTMyNjczMDc0MjExODg5Mi0zMzU3NTA5MTU5ODEwNzA>FUNDAMENTALS OF INVESTMENT</a></b>

<b><a href=https://t.me/ExamWalletBot?start=Z2V0LTM0MTc2NDM2NTIyMjUyMi0zNDg3ODAwNTYwMDQyMTY>INCOME TAX & GST</a></b>

<i>Click on the subject name to view available resources.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCM2019PYQSEMESTERS = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Course Selected:</b> BCOM  

Now, choose your semester to access <b>previous year question papers.</b>

<b><i>@ExamWalletBot</i></b>"""

    BCMPYQSEM1 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> First  

Previous year question papers will be <b>added soon.</b>  

<i>Click on the subject name to view available papers.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCMPYQSEM2 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> Second  

Previous year question papers will be <b>added soon.</b>  

<i>Click on the subject name to view available papers.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCMPYQSEM3 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> Third  

Previous year question papers will be <b>added soon.</b>  

<i>Click on the subject name to view available papers.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCMPYQSEM4 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> Fourth  

Previous year question papers will be <b>added soon.</b>  

<i>Click on the subject name to view available papers.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCMPYQSEM5 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> Fifth  

Previous year question papers will be <b>added soon.</b>  

<i>Click on the subject name to view available papers.</i>

<b><i>@ExamWalletBot</i></b>"""

    BCMPYQSEM6 = """<u><b>𝙀𝙭𝙖𝙢𝙒𝙖𝙡𝙡𝙚𝙩</b></u>

<b>Semester:</b> Sixth  

<b><a href=https://t.me/ExamWalletBot?start=Z2V0LTMwODY5MDM5NDM5NDUzNi0zMTI2OTkzNjA1NTU1MDQ>FINANCIAL DERIVATIVES</a></b>

<b><a href=https://t.me/ExamWalletBot?start=Z2V0LTMyMTcxOTUzNDQxNzY4Mi0zMjU3Mjg1MDA1Nzg2NTA>AUDITING AND CORPORATE GOVERNANCE</a></b>

<b><a href=https://t.me/ExamWalletBot?start=Z2V0LTMzNjc1MzE1NzUyMTMxMi0zNDA3NjIxMjM2ODIyODA>FUNDAMENTALS OF INVESTMENT</a></b>

<b><a href=https://t.me/ExamWalletBot?start=Z2V0LTM0OTc4MjI5NzU0NDQ1OC0zNTM3OTEyNjM3MDU0MjY>INCOME TAX & GST</a></b>

<i>Click on the subject name to view available papers.</i>

<b><i>@ExamWalletBot</i></b>"""
    
