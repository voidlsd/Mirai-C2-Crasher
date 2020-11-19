# Mirai C2 Crasher
Mirai C2 Crasher exploits a certain part of the code to cause buffer overflow.
# Where is the vulnerability?
Right in [here](https://github.com/jgamblin/Mirai-Source-Code/blob/master/mirai/cnc/admin.go), In line number 39, where it states  ```username, err := this.ReadLine(false)```  which will retrieve the username and password you entered in the C2 and does a Readline which basically reads a line and then it will run it to line number 225, where it states: ```go buf := make([]byte, 1024)```, which means if the login letters are bigger than "1024" it will cause buffer overflow, which will basically override the memory and corrupt the data values that it was originally addressed to and crash the C2. Also, Since most mirais are "variants" of each other, I believe this vulnerability is on all Mirai variants but complied in a different way.
# Where did you find the vulnerability?
I wasn't the founder of the vulnerability, you can find the original vulnerability explained [here](https://www.ankitanubhav.info/post/crash).
# How do I use it?
You simply enter the C2 IP and the C2 port, and it'll run the exploit. <br>
credits to other Mirai C2/CnC Crashers on GitHub, I had to reference a lot. <br>
Update: I fixed it, I have no idea why I created a thread and tried to bring a function as a variable.
