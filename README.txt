Hello. I'm Atlas Yang.
Thank you for using my program.
If you have any questions, It will be great if you send it to my email below.
Email: epsilon2718@naver.com
         gilmo.yang0203@gmail.com
Github: 

Requirements
1. Python 3.7 or up (This code is written in Python 3.7)
2. Numpy
3. Pygame 1.9.6

Instruction
1. Customize the code.
  - In line 35-37, you can customize the color of each state, and grid line color.
  - In line 88-94, you see T, the state transition matrix. Function process_alternative (which is activated by n key) is based on 
   Tns method. (Please Check my Reddit article.)
2. Execute the code.
  - Try using 'execute.bat' or command prompt. Python IDLE may not work well.
3. Input width, height, and cell size by pixel.
  - Program works best when cell size is common divisor of width and height. Consider using the numbers below.
    - 720/540/10, 1080/630/15, 1720/1080/20
4. Simulate.
  - Click any cell to change state. If the rule have more than 2 available states, just click one more time for another state.
 - Press n to process 1 step with alternative rule.
 - Press m to precess 1 step with original rule.