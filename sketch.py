'''
Jenisha Patel, 760284
ICS3U0 Final Project - January 2024
'''

def setup(): #Defining any global values & setting up screen & background, making buttons to change the slides
    global x1, y1, x2, y2
    global speedX1, speedY1, speedX2, speedY2
    global step
    global a, dA, r, g, b, c
    global question

    x1, y1 = 16, 16
    speedX1, speedY1 = 2, 5
    x2, y2 = width - 16, 16
    speedX2, speedY2 = 5, 2

    a = 0
    dA = 2
    r = [255,   0,   0,   0, 255, 255, 255, 255]
    g = [255,   0, 255, 255,   0,   0, 255, 255]
    b = [20, 255,   0, 255,   0, 255,   0, 255]
    c = 0

    step = 0
    question = 0
 # ⬆ Initlizing any Global Varibales I have

    size(600,600) 
    background(252, 243, 217)
    fill(247, 247, 245)
    rect(20, 520, 100, 50, 8)
    rect(480, 520, 100, 50, 8)
 # ⬆ Setting up my screen & making the two main buttons I used   
    
def draw(): #drawing background & where the slide is changed by using the step variable also has the buttons to change slides 
    global question
    background(252, 243, 217)

    if step == 0:
        first()
    elif step == 1:
        second()
    elif step == 2:
        third()
    elif step == 3:
       fourth()
    elif step == 4:
        fifth()
    elif step == 5:
        sixth()
    elif step == 6:
        seventh()
    elif step == 7:
        eigth()
    elif step == 8:
        nineth()
    elif step == 9:
        tenth()
        question = 0
    elif step == 10:
        quiz()
    elif step == 11:
        eleventh()    
 # ⬆ Above is how the slides are changed by using the step values

    fill(247, 247, 245)
    rect(20, 520, 100, 50, 8)
    rect(480, 520, 100, 50, 8)
    fill(0, 0, 0)
    text("PREV.", 25, 555)
    text("NEXT", 487, 555)
    textSize(32) 
 # ⬆ Above is how my previous slide & next slide buttons have been coded

def keyPressed(): #How the slides are changed by pressing the arrow keys, as well as how the quiz slides change when the space & del keys are pressed
    global step, question 

    if key == 65535:
        if keyCode == 37 or keyCode == 40:
            step = step - 1
            if step < 0:
                step = 0
        elif keyCode == 38 or keyCode == 39:
            step = step + 1
            if step > 11:
                step = 11
        else:
            pass
 # ⬆ Above is how the main information slides change when the arrow keys are pressed

    if keyCode == 32:
        question = question + 1
        if question > 4:
            question = 4
    elif keyCode == 8:
        question = question - 1
        if question < 0:
            question = 0
    else:
        pass
  # ⬆ Above is how the question slide which are inside the quiz function change by using the space & del keys

    #print("KeyCode:", keyCode) - I used this code to help me find the ASCII values for certain keys

def mouseClicked(): #how the slides are chnaged by useing the drawn buttons
    global step

    if mouseX >= 20 and mouseX <= 100 and mouseY >= 520 and mouseY <= 570:
        step = step - 1
        if step < 0:
            step = 0
    elif mouseX >= 480 and mouseX <= 580 and mouseY >= 520 and mouseY <= 570:
        step = step + 1
        if step > 11:
            step = 11
    else:
        pass
 # ⬆ Above is how the main slides change when the Previous slide & Next slide buttons are pressed

def first(): #Title page, includes project & creator name as well as an animated image
    fill(0, 0, 0)
    textSize(40)
    text("Computer Science Prospects", 15, 70)
    textSize(32)
    text("After High School", 170, 120)
    textSize(24)
    text("Jenisha Patel | ICS3U0 - R", 150, 550 )
    text("Final Project", 230, 580 )
 # ⬆ Above is all of the text on my Title slide 

    img2 = loadImage("imageTwo (1).jpg")
    image(img2, 270, 170)
    img3 = loadImage("imageThree.jpg")
    image(img3, 270, 330)
    animted_elements_title()
 #This is all the code for the images on the tilte slide, i used a function to add in the moving inmage as you see below 

    textSize(32)

def animted_elements_title(): #Animated images for the title slide comes in & stops at a certain point
    global x1, y1, x2, y2
    global speedX1, speedY1, speedX2, speedY2
    
    x1 = x1 + speedX1
    y1 = y1 + speedY1
    x2 = x2 + speedX2
    y2 = y2 + speedY2
 
    if x1 > width-16 or x1 < 16:
        speedX1 = speedX1 * -1
    if y1 > height-16 or y1 < 16:
        speedY1 = speedY1 * -1
    if x2 > width-16 or x2 < 16:
        speedX2 = speedX2 * -1
    if y2 > height-16 or y2 < 16:
        speedY2 = speedY2 * -1
 # ⬆ Defining the speed for the x1, x2, y1, y2 variables and preeventing them from going off the page

    img = loadImage("imageOne (3).jpg")
    if y2 >= 170:
        image(img, 40, 170 )
        y2 = 170
    else:
        image(img, 40, y2 )
 
 # ⬆ Moving Image
 
def second(): #Second slide which is table of contents - in a list and uses a for loop to display, contains moving image along the x aixs also includes a function to move elements around
    global x1, y1, x2, y2
    global speedX1, speedY1, speedX2, speedY2
    
    x1 = x1 + speedX1
    y1 = y1 + speedY1
    x2 = x2 + speedX2
    y2 = y2 + speedY2

    if x1 > width-16 or x1 < 16:
        speedX1 = speedX1 * -1
    if y1 > height-16 or y1 < 16:
        speedY1 = speedY1 * -1
    if x2 > width-16 or x2 < 16:
        speedX2 = speedX2 * -1
    if y2 > height-16 or y2 < 16:
        speedY2 = speedY2 * -1
 # ⬆ Defining the speed for the x1, x2, y1, y2 variables and preeventing them from going off the page

    animted_elements1()
 # ⬆ This code has three moving cirles that use parts of the above code to move around at differnt speeds

    fill(0,0,0)
    textSize(40)
    text("Table Of Contents", 110, 60)
    textSize(15)
    text("Post Secondary Education & Career Prospects for a Job in Computer Studies", 15, 90)
    textSize(18)
 # ⬆ Any Texton my page outside of the table of contents

    lines = [
    "What is Computer Studies",
    "What can you do with a degree in Computer Studies", 
    "Post Secondary Education Prospects 	", 
    "Components of Computer Studies Programs", 
    "Benefits of Pursuing Computer Studies",
    "Careers in Computer Studies", 
    "Industry Trends and Innovations ", 
    "Conclusion ",
    ]

    for i, line in enumerate(lines):
        x = 25
        y = 120 + 25 * i
        text(line, x, y)

 # ⬆ all the text in the table of contents using a list to store the conetents & printing them onto the screen using a for loop

    textSize(32)
    img4 = loadImage("imageFour.jpg")
    image(img4, x1 , 310)
    textSize(32)
 # ⬆ Moving Image

def animted_elements1(): #Creates three differnet circles which move around at differnt speeds
    global x1, y1, x2, y2
    global speedX1, speedY1, speedX2, speedY2
    
    x1 = x1 + speedX1
    y1 = y1 + speedY1
    x2 = x2 + speedX2
    y2 = y2 + speedY2

    if x1 > width-16 or x1 < 16:
        speedX1 = speedX1 * -1
    if y1 > height-16 or y1 < 16:
        speedY1 = speedY1 * -1
    if x2 > width-16 or x2 < 16:
        speedX2 = speedX2 * -1
    if y2 > height-16 or y2 < 16:
        speedY2 = speedY2 * -1
 # ⬆ Defining the speed for the x1, x2, y1, y2 variables and preeventing them from going off the page

    stroke(0)
    fill(196, 202, 242)
    ellipse(x1, y1, 50, 50)

    stroke(0)
    fill(242, 196, 232)
    ellipse(x2, y2, 50, 50)

    stroke(0)
    fill(196, 242, 215)
    ellipse(y2, x1, 50, 50)
 # ⬆ three circles are drawn moving around at differwnt speeds

def third(): #First infromation slide, talks about what computer studies is and has a moving image
    global x1, y1, x2, y2
    global speedX1, speedY1, speedX2, speedY2
    
    x1 = x1 + speedX1
    y1 = y1 + speedY1
    x2 = x2 + speedX2
    y2 = y2 + speedY2

    if x1 > width-16 or x1 < 16:
        speedX1 = speedX1 * -1
    if y1 > height-16 or y1 < 16:
        speedY1 = speedY1 * -1
    if x2 > width-16 or x2 < 16:
        speedX2 = speedX2 * -1
    if y2 > height-16 or y2 < 16:
        speedY2 = speedY2 * -1
 # ⬆ Defining the speed for the x1, x2, y1, y2 variables and preeventing them from going off the page

    img5 = loadImage("imageFive (1).jpg")
    image(img5, x1 , 15 )
    textSize(32)
    text("What is Computer Studies", 95, 395)
    textSize(15)
    txt_compstudies_info = ("Computer Studies is the study of computer hardware and software. It is a field which includes everything from the algorithms that make up software to how software interacts with hardware to how well software is developed and designed.")
    text(txt_compstudies_info, 30, 410, 535, 150)
    textSize(32)
 # ⬆ First Imformation Side - talks about what computer science is 

def fourth(): #Second information slide, talks about what you can do with a computer science degree & has a funtion to move images around
    textSize(34)
    text("What can you do with a degree in ", 15, 55)
    text("Computer Studies", 150, 90)
    textSize(15)
    txt_compstudiesdegree_info = ("You can do a lot of things with a computer studies degree such as becoming a software developer or engineer, one of the many types of programmers, such as applications, systems & multimedia, a web designer as well as one of many types of engineers, such as software or computer. Knowing more about computers will be useful in the future as technology is slowly taking over the planet so knowing how to program & functions of computers will be useful in the future.")
    text(txt_compstudiesdegree_info, 30, 110, 535, 180)
 # ⬆ Second Information slide - talks about what you can do with a computer science degree

    animted_elements2()
 # ⬆ Code to add moving elements(images)
    textSize(32)

def animted_elements2(): #Moves and images along the x axis at a certain speed - for the second information slide
    global x1, y1, x2, y2
    global speedX1, speedY1, speedX2, speedY2
    
    x1 = x1 + speedX1
    y1 = y1 + speedY1
    x2 = x2 + speedX2
    y2 = y2 + speedY2

    if x1 > width-16 or x1 < 16:
        speedX1 = speedX1 * -1
    if y1 > height-16 or y1 < 16:
        speedY1 = speedY1 * -1
    if x2 > width-16 or x2 < 16:
        speedX2 = speedX2 * -1
    if y2 > height-16 or y2 < 16:
        speedY2 = speedY2 * -1
 # ⬆ Defining the speed for the x1, x2, y1, y2 variables and preeventing them from going off the page

    stroke(0)
    img6 = loadImage("Untitled design (1).jpg")
    image(img6, x1 , 310)
 # ⬆ Moving Image

def fifth(): #Third infromation slide, talks about what you can do for post secondary in this field 
    textSize(32)
    text("Post Secondary Education Prospects  ", 15, 55)
    textSize(12)
    txt_post_secondayedu = (" Many post-secondary institutions offer Computer Science as a major and and minor and sometimes even a double major. Schools also typically allow you to begin with the basics and learn more about what to specialize in later on. Some of the different post-secondary programs that have either a major or minor in computer science are Computer Science, Software & Computer Engineering, Computing Technology, Information Systems and Programming. A few double major programs would be Mathematics and Computer Science and Business Administration and Computer Science. Some of the things you can specialize in are Algorithms, Computer and Internet Security, Mobile Computing, Computer Game Development, Network Computing, Data Science and Management and Entrepreneurship.  ")
    text(txt_post_secondayedu, 30, 85, 535, 200)
 # ⬆ Third Information Slide - talks about the post secondary eduation prospects of computer science

    img7 = loadImage("Untitled design (2).jpg")
    image(img7, 50, 300)
    textSize(32)

def sixth(): #Fourth information slide, talks about the different componets, or things you'll learn in the program, has a funtion to show moving imgages
    textSize(32)
    text("Components of Computer Studies", 25, 55)
    text(" Programs ", 200, 90)
    textSize(15)
    txt_componetsofcompstudies = ("Some of the things you’ll learn about in computer study programs are artificial intelligence, computer systems and networks, security, database systems, vision and graphics, numerical analysis, programming languages, software engineering, bioinformatics and theory of computing.")
    text(txt_componetsofcompstudies, 30, 110, 535, 200)
 # ⬆ Fourth Infornation slide - talks about what you will learn in computer science programs

    componetsofcompstudies_img()
 # ⬆ Code for moving images 
    
    textSize(32)

def componetsofcompstudies_img(): #Function to move two images at different speeds along the y aixs and stopping them when they get to a certain point
    global x1, y1, x2, y2
    global speedX1, speedY1, speedX2, speedY2
    
    x1 = x1 + speedX1
    y1 = y1 + speedY1
    x2 = x2 + speedX2
    y2 = y2 + speedY2

    if x1 > width-16 or x1 < 16:
        speedX1 = speedX1 * -1
    if y1 > height-16 or y1 < 16:
        speedY1 = speedY1 * -1
    if x2 > width-16 or x2 < 16:
        speedX2 = speedX2 * -1
    if y2 > height-16 or y2 < 16:
        speedY2 = speedY2 * -1
 # ⬆ Defining the speed for the x1, x2, y1, y2 variables and preeventing them from going off the page

    img11 = loadImage("Untitled design (2).png")
    if y1 >= 250:
        image(img11, 5, 250)
        y1 = 250
    else:
        image(img11, 5, y1)
    img12 = loadImage("imageSIX.jpg")
    if y2 >= 250:
        image(img12, 300, 250)
        y2 = 250
    else:
        image(img12, 300, y2)
 # ⬆ having images moving to a ceritan point and then stopping

def seventh():#Fifth information slide, talks about what are the benifits of pursing computer science are & the text & image are shown only when the title reachs a certain ponit
    global x1, y1, x2, y2
    global speedX1, speedY1, speedX2, speedY2
    
    x1 = x1 + speedX1
    y1 = y1 + speedY1
    x2 = x2 + speedX2
    y2 = y2 + speedY2

    if x1 > width-16 or x1 < 16:
        speedX1 = speedX1 * -1
    if y1 > height-16 or y1 < 16:
        speedY1 = speedY1 * -1
    if x2 > width-16 or x2 < 16:
        speedX2 = speedX2 * -1
    if y2 > height-16 or y2 < 16:
        speedY2 = speedY2 * -1
 # ⬆ Defining the speed for the x1, x2, y1, y2 variables and preeventing them from going off the page

    textSize(30)
    if y2 >= 500:
        text("Benefits of Pursuing Computer Studies", 15, y2)
        y2 = 500
    else:
        text("Benefits of Pursuing Computer Studies", 15, y2)
  # ⬆ Code to move the title into a certain positon & keeping it there
    
    if y2 == 500:
        img9 = loadImage("Untitled design (3).png")
        image(img9, 0, 0)
        textSize(15)
        txt_benifitsofcompstudies = ("Some of the benefits of pursuing a computer science degree are that since we basically depend on technology, and computers for our day-to-day lives any job dealing with technology is in high demand right now. After graduating there is a good chance you will be able to find a job within 15 months of graduating sometimes even sooner, and since people who have knowledge of computers are in high demand in every industry, you will probably get a good starting salary. ")
        text(txt_benifitsofcompstudies, 30, 270, 535, 200)
 # ⬆ Fifth Infromation slide - talks about the benifts of pursuing computer sciene
    textSize(32)
 # ⬆ Code to show everything after the title has reached a certain ponit (500- on y axis)

def eigth(): #Sixth Information slide, talks about the different careers in computer science, has a feature have the image on the slide follow your mouse 
    text("Careers in Computer Studies ", 75, 55)
    img8 = loadImage("comp sci carrers.png")
    image(img8, mouseX - img8.width/2, mouseY - img8.height/2)
 # ⬆ Code to have the image follow your mouse around
    textSize(15)
    carrersincompstudies_txt = ("Some different careers you could do in the field of computer studies are becoming a software or computer engineer, a programmer,  as well systems & multimedia, or a web designer, however, these are only a few of the options you have with a degree in computer studies since this field is slowly becoming one of the most in-demand fields.  ")
    text(carrersincompstudies_txt, 30, 310, 535, 150)
    mousefollow_txt = ("This slide's image will follow your mouse around")
    text(mousefollow_txt, 130, 585 )
 # ⬆ All the text for the Sixth infromation slide - talks about the different carrers you could do with a degree in computer science

    textSize(32)

def nineth(): #Seventh Infromation slide, talks about the trends & invoations of computer studies
    text("Industry Trends and Innovations ", 60, 55)
    industrytrendsninvovations_txt = ("In computer science, some of the ongoing trends include advancements in AI and ML, the rise of edge computing, the development of quantum computing, 5G technology applications, innovations in cybersecurity, blockchain, AR/VR technologies, and the intersection of biotechnology with computational biology. Standard practices like DevOps and CI/CD are enhancing software development, while RPA is automating business processes. These trends highlight the field's transformative impact across diverse industries.")
    textSize(15)
    text(industrytrendsninvovations_txt, 30, 310, 535, 200)
    img14 = loadImage("img14.png")
    image(img14,40,90 )
    textSize(32)
 # ⬆ Seventh Information Slide - talks about some of the trends & invations of the computer science feild

def tenth(): #concluison slide, gives a breif summery of what my presentaion talked about
    textSize(40)
    text("Conclusion", 200, 50)
    textSize(15)
    conclusin_txt = ("In conclusion, getting a computer studies degree offers diverse career paths in the tech world, from software development to web design. The demand for these skills is high, leading to quick job placements and high salaries. Ongoing trends in AI, cybersecurity, and other technologies emphasize the engaged nature of the field. In a world increasingly reliant on technology, a computer studies degree opens doors to a promising and in-demand future.")
    text(conclusin_txt, 20, 120, 530, 200 )
    img13 = loadImage("image10.png")
    image(img13, 100, 340)
    textSize(32)
 # ⬆ Concluison slide - Summary Of what i Talked about in my presention

def quiz(): #My Mini Quiz at the end, contains 5 questions & will only be shown after an image reaches a certain ponit
    global x1, y1, x2, y2
    global speedX1, speedY1, speedX2, speedY2
    global question

    x1 = x1 + speedX1
    y1 = y1 + speedY1
    x2 = x2 + speedX2
    y2 = y2 + speedY2

    if x1 > width-16 or x1 < 16:
        speedX1 = speedX1 * -1
    if y1 > height-16 or y1 < 16:
        speedY1 = speedY1 * -1
    if x2 > width-16 or x2 < 16:
        speedX2 = speedX2 * -1
    if y2 > height-16 or y2 < 16:
        speedY2 = speedY2 * -1
 # ⬆ Defining the speed for the x1, x2, y1, y2 variables and preeventing them from going off the page

    if step != 10:
        x2 = 16 + speedX2
    else:
        pass #reseting the x2 value if step != 10

    questionsimg = loadImage("quizimage.jpg")
    if x2 >= 550:
        image(questionsimg, x2, 0)
        x2 = 550
    else:
        image(questionsimg, x2, 0)
 # ⬆ Moving Images & having it Stop at a certain Point

    if x2 == 550: #Everything being shown after the x2 & image have a value of 550
        quiz = ["Q", "U", "E", "S", "T", "I", "O", "N", "S" ]
        for q, letters in enumerate(quiz):
            x = 50 + 50 * q
            y = 95
            textSize(55)
            text(letters, x, y)
     # Question Title used a list & for loop to progam each letter to come in at a different x value

        fill(247, 205, 236)
        rect (450, 420, 55, 55, 7)
        rect (450, 350, 55, 55, 7)
        rect (450, 280, 55, 55, 7)
        rect (450, 210, 55, 55, 7)
     # Boxes for the choices

        fill(0,0,0)
        choices = ["A", "B", "C", "D"]
        for a, option in enumerate(choices):
            y = 260
            y = y + 70 * a
            x = 460
            textSize(50)
            text(option, x, y)
         # Choices -A, B, C, D used a list & for loop to progam each letter to come in at a different y value
        fill(247, 247, 245)
        rect(30, 400, 405, 100, 7)
     #Awanser Box

        fill(0,0,0)
        textSize(15)
        text("Please select the option you chose above", 130, 575 )

        textSize(15)
        text("Press Space to continue & Del to go back", 90, 495 )

        if question == 0:
            questionOne()
        elif question == 1:
            questionTwo()
        elif question == 2:
            questionThree()
        elif question == 3:
            questionFour()
        elif question == 4:
            questionFive()
    #Question Steps programed to move using the space and del keys
           
    textSize(32)

def questionOne():#First Question in my mini Quiz - Has lsit of options & you must click the box of which awaner your chose then use space to change to change questions once done
    firstquestion = ("What is one of the benefits of pursuing a degree in computer studies?")
    textSize(20)
    text(firstquestion, 25, 120, 520, 200)

    Q1_awnser_options = [
        "A: Can easily get a job and high salries",
        "B: Oppourtunites to travel & learn more",
        "C: Can have to oppourtunity to learn many versitle skills",
        "D: Your skill will be needed in all industries"
    ]

    for a, option in enumerate(Q1_awnser_options):
        y = 210 + 45 * a
        x = 45
        textSize(15)
        text(option, x, y, 405, 50)

    button_A_Correct()
    button_B_Correct()
    button_C_Correct()
    button_D_Correct()
    
    textSize(32)

def questionTwo(): #Second Question in my mini Quiz - Has lsit of options & you must click the box of which awaner your chose then use space to change to change questions once done
    secondquestion = ("What can you specialize in after learning the basic aspects of computer science?")
    textSize(20)
    text(secondquestion, 25, 120, 520, 200)

    Q2_awnser_options = [
        "A: Algorithms, Computer & Internet Security, Network Computing",
        "B: Fashion Design",
        "C: Computer Game Development",
        "D: Medical Feild"
    ]

    for a, option in enumerate(Q2_awnser_options):
        y = 210 + 45 * a
        x = 45
        textSize(15)
        text(option, x, y, 405, 50)

    button_A_Correct()
    button_B_Wrong()
    button_C_Correct()
    button_D_Wrong()
    
    textSize(32)

def questionThree(): #Third Question in my mini Quiz - Has lsit of options & you must click the box of which awaner your chose then use space to change to change questions once done
    thirdquestion = ("What is Computer Studies?")
    textSize(20)
    text(thirdquestion, 25, 120, 520, 200)

    Q3_awnser_options = [
        "A: The study of aestheics & design",
        "B: The study of computers & thier components",
        "C: The study of finaces & business",
        "D: The study of aviation & planes"
    ]

    for a, option in enumerate(Q3_awnser_options):
        y = 210 + 45 * a
        x = 45
        textSize(15)
        text(option, x, y, 405, 50)

    button_A_Wrong()
    button_B_Correct()
    button_C_Wrong()
    button_D_Wrong()

    textSize(32)

def questionFour():#Fourth Question in my mini Quiz - Has lsit of options & you must click the box of which awaner your chose then use space to change to change questions once done
    fourthquestion = ("What are some careers you can pursue after post-secondary with a computer studies degree?")
    textSize(20)
    text(fourthquestion, 25, 120, 520, 200)

    Q4_awnser_options = [
        "A: A software or computer engineer or a programmer",
        "B: A Doctor or Surgeon ",
        "C: A Pilot",
        "D: An systems or multimedia or web designer"
    ]

    for a, option in enumerate(Q4_awnser_options):
        y = 210 + 45 * a
        x = 45
        textSize(15)
        text(option, x, y, 405, 50)

    button_A_Correct()
    button_B_Wrong()
    button_C_Wrong()
    button_D_Correct()

    textSize(32)

def questionFive(): #Fifth Question in my mini Quiz - Has lsit of options & you must click the box of which awaner your chose then use space to change to change questions once done
    fifthquestion = ("What are some of the things you’ll learn in post-secondary programs for computer studies?")
    textSize(20)
    text(fifthquestion, 25, 120, 520, 200)

    Q5_awnser_options = [
        "A: Artificial Intelligence(AI) ",
        "B: About vision and graphics",
        "C: Multiple programming languages",
        "D: Software engineering & computer systems and networks security"
    ]

    for a, option in enumerate(Q5_awnser_options):
        y = 210 + 45 * a
        x = 45
        textSize(15)
        text(option, x, y, 405, 50)

    button_A_Correct()
    button_B_Correct()
    button_C_Correct()
    button_D_Correct()
    
    textSize(32)

def button_A_Correct(): #showes the word correct when hovering over the A button
    if 450 <= mouseX <= 505 and 210 <= mouseY <= 265:
        textSize(50)
        text("CORRECT!!", 40, 400, 300, 100)

def button_A_Wrong():#showes the word wrong when hovering over the A button
    if 450 <= mouseX <= 505 and 210 <= mouseY <= 265:
        textSize(50)
        text("Wrong :(", 40, 400, 300, 100)

def button_B_Correct():#showes the word correct when hovering over the B button
    if 450 <= mouseX <= 505 and 280 <= mouseY <= 335:
        textSize(50)
        text("CORRECT!!", 40, 400, 300, 100)

def button_B_Wrong(): #showes the word wrong when hovering over the B button
    if 450 <= mouseX <= 505 and 280 <= mouseY <= 335:
        textSize(50)
        text("Wrong :(", 40, 400, 300, 100)

def button_C_Correct(): #showes the word correct when hovering over the C button
    if 450 <= mouseX <= 505 and 350 <= mouseY <= 405:
        textSize(50)
        text("CORRECT!!", 40, 400, 300, 100)

def button_C_Wrong():#showes the word wrong when hovering over the C button
    if 450 <= mouseX <= 505 and 350 <= mouseY <= 405:
        textSize(50)
        text("Wrong :(", 40, 400, 300, 100)

def button_D_Correct(): #showes the word correct when hovering over the D button
    if 450 <= mouseX <= 505 and 420 <= mouseY <= 455:
        textSize(50)
        text("CORRECT!!", 40, 400, 300, 100)

def button_D_Wrong(): #showes the word wrong when hovering over the D button
    if 450 <= mouseX <= 505 and 420 <= mouseY <= 455:
        textSize(50)
        text("WRONG :( ", 40, 400, 300, 100)

def eleventh(): #Final sldide which has a function to make the background change colors and has an image
    background_fade()
    fill(0,0,0)
    ellipse(300, 300, 75, 75)
    img10 = loadImage("image-removebg-preview.png")
    image(img10, 25, 70)

def background_fade(): #changes how the background changes color in my last slide

    global a, dA, r, g, b, c

    a = a + dA
    if a >= 256:
        dA = dA * -1
    elif a <= 0:
        dA = dA * -1
        c = int(random(0, len(r)))
    
    fill(r[c], g[c], b[c], a)
    rect(0, 0, 600, 600)
 #Changing color Background

'''
Include Reaserch Doc & Code Journal Link
'''