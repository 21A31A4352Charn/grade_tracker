import openpyxl
def getrollnumber():
        path=r"C:\Users\murak\Python programs\Book2.xlsx"
        file=openpyxl.load_workbook(path)
        sheet=file.active
        roll=[]
        for cell in sheet.iter_rows(min_row=1,max_row=145,min_col=1,max_col=2,values_only=True):
            roll.append(cell)
        return roll
def getdate():
        return "2023-03-09"

def passwords(password):
        l=len(password)
        print(l)
        print(password.isupper())
        if (l==10 and password.isupper()):
                return True
        
        else:
                return False

def uppercase(username):
        return username.upper()


def forginkeys(username):
        try:
                s=student.objects.get(username=username).bools
                print(s)
                if (s==False):
                        m=student.objects.get(username=username)
                        m.marks=username
                        m.bools=True
        except:
                pass

'''<br>
      <form method="POST" action="enter">
        {% csrf_token %}
      <button type="submit" class="btn btn-success">Relese Marks</button>
    </form>'''

