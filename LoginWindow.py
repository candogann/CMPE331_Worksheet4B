"""
    Stage: Development-01
    @author: Ali Can Doğan, 120200068
    @author: Ahmed Ibrahim Attya Hamouda, 120200006
    @author: Çağatay Yaman, 120200029
""" 

import tkinter as tk


class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login Page") # sets the window name "Login Page"
        
        # init gui and place them on window
        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        #ADD labels
        self.lblUsername = tk.Label(text="Username")
        self.lblPassw = tk.Label(text="Password")
        # add text
        self.txtUsername = tk.Entry()
        self.txtPassw = tk.Entry()
        #add buttons
        self.btnLogin = tk.Button(text="Login")
        self.btnExit = tk.Button(text="Exit")
        #bind buttons (or other elements u wanna use) to click handler
        self.btnLogin.bind("<Button-1>", self.handle_click)
        self.btnExit.bind("<Button-1>", self.handle_click)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        #add gui elements to frame
        self.lblUsername.grid(row=0, column=0, padx=10, pady=5)
        self.txtUsername.grid(row=0, column=1, padx=10, pady=5)

        self.lblPassw.grid(row=1, column=0, padx=10, pady=5)
        self.txtPassw.grid(row=1, column=1, padx=10, pady=5)

        self.btnLogin.grid(row=2, column=0, padx=10, pady=5)
        self.btnExit.grid(row=2, column=1, padx=10, pady=5)

    """
        An attempt to login, you give input creds to this method and it will return True or False

        :param username: user's username
        :param passw: user's password
        :returns: True, False
    """
    def attemptLogin(self,username,passw):
        
        if username == "test" and passw == "test":
            return True
            # ...
        else:
            return False

    
    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        # if event's widget is from btnLogin, get username and password from textbox and attempt to login
        # if true, destroy the page and direct to newpage
        if event.widget == self.btnLogin:
            if self.attemptLogin(self.txtUsername.get(),self.txtPassw.get()):
                self.window.destroy()
                NewPage()
            else:
                print("wrong creds")
        # if widget is exit, destroys the window
        if event.widget == self.btnExit:
            self.window.destroy()
        

class NewPage:
    #constructor 
    def __init__(self):
        self.window = tk.Tk() # root window, if you wanna destroy the frame, use this variable
        self.window.title("New Page")

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()
    
    def _initializeGUI(self):
        self.lblLoggedin = tk.Label(text="Successfully logged in") 

    def _addGUIElementsToFrame(self):
        self.lblLoggedin.grid(row=0, column=0, padx=10, pady=5)



# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
