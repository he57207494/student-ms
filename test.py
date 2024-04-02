from service import service

result = service.exec("insert into tb_grade(gradeID,gradeName) values(%s,%s)",(4,"初四"))

print(result)