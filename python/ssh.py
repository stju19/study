import paramiko


class SSH_Operation(object):
     def __init__(self,ip,name,password):
         self.hostname=ip
         self.username=name
         self.password=password
         self.s=paramiko.SSHClient()
         self.s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         #self.s=pxssh.pxssh()

     def SSH_Login(self):
        print "start to login"
        self.s.connect(self.hostname,22,self.username, self.password)
        print "Login %s:%s:%s" % (self.hostname,self.username,self.password)
        #self.s.login(self.hostname, self.username, self.password, original_prompt='[$#>]')

     def SSH_Write(self, str):
        print "start to write"
        import pdb;pdb.set_trace()
        stdin, stdout, stderr=self.s.exec_command(str)
        # stdin.write("1111\n")
        #self.s.before = stdout.readlines()
        print stdout.readlines()
        print stderr.readlines()
        #self.s.sendline(str)
        #self.s.prompt()

     def SSH_Read(self):
         print "start to read"
         return self.s.before

     def SSH_Logout(self):
         #self.s.logout()
         self.s.close()


def main(req):
    return render(req, "main.html");


def cpu_pressure():
    print "Enter cpu pressure"
    foo = SSH_Operation("10.43.167.105", "root", "ossdbg1")
    foo.SSH_Login()
    foo.SSH_Write("/home/test.sh &>/dev/null &")

cpu_pressure()
