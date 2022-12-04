from celery import shared_task
from django.contrib.auth.models import User
from io import BytesIO
import xlwt
from django.core.mail import EmailMessage

@shared_task(bind=True)
def send_excel(self, email):
    excelfile = BytesIO()
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheetname')

    row = 0
    users = User.objects.all()

    for i in users:
        ws.write(row, 0, i.id)
        ws.write(row, 1, i.username)
        ws.write(row, 2, i.is_active)
        row+=1
    
    wb.save(excelfile)

    email = EmailMessage('Hello', 'User excel attachment', 'shivam.wolfpack@gmail.com', [email])
    email.attach('file.xls', excelfile.getvalue() , 'application/ms-excel')
    email.send()