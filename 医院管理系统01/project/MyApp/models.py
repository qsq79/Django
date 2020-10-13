from django.db import models


class Dept(models.Model):#科室信息表
    dept_name = models.CharField(max_length=20)#科室名称
    dept_manager = models.CharField(max_length=20)#科长
    dept_manager_telep = models.CharField(max_length=20)#科长电话
    dept_floor = models.CharField(max_length=20)#科室楼层
    def __str__(self):
        return self.dept_name

class Patient(models.Model):#病人信息表
    patient_name = models.CharField(max_length=20)#病人姓名
    patient_sex = models.CharField(max_length=10)#病人性别
    patient_age = models.CharField(max_length=10)#病人年龄
    patient_telep = models.CharField(max_length=20)#病人电话
    patient_idcard = models.CharField(max_length=30)#病人身份证号
    patient_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)#病人问诊科室
    def __str__(self):
        return self.patient_name

class Doctor(models.Model):#医生信息表
    doctor_id = models.CharField(max_length=20)#医生编号
    doctor_name = models.CharField(max_length=20)#医生姓名
    doctor_sex = models.CharField(max_length=20)#医生性别
    doctor_age = models.CharField(max_length=20)#医生年龄
    doctor_telep = models.CharField(max_length=20)#医生电话
    doctor_position = models.CharField(max_length=20)#医生职位
    doctor_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)#医生所在科室
    def __str__(self):
        return self.doctor_name


class Room(models.Model):#病房信息表
    room_id = models.CharField(max_length=10)#床铺编号
    room_patient_id = models.CharField(max_length=20)#病人问诊号
    room_patient_name = models.CharField(max_length=20)#病人姓名
    room_patient_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)#病房所在科室（XX科的病房）
    def __str__(self):
        return self.room_patient_name


class Work(models.Model):#医生值日表
    work_doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)#值日医生编号
    work_doctor_name = models.CharField(max_length=20)#值日医生姓名
    work_time = models.CharField(max_length=20)#工作时间
    work_doctor_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)#值日表所在科室（XX科的值日表）
    def __str__(self):
        return self.work_doctor_name

class Deal_method(models.Model):#医生处理方案表
    deal_patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)#病人的问诊号
    deal_room_id = models.CharField(max_length=20)#病人的房号
    deal_doctor_name = models.CharField(max_length=20)#问诊医生姓名
    medicine_detail = models.CharField(max_length=50)#用药详情
    diagnosis_time = models.CharField(max_length=20)#诊断时间
    diagnosis_result = models.CharField(max_length=50)#诊断结果
    doctor_suggestions = models.CharField(max_length=50)#医生建议
    def __str__(self):
        return self.deal_doctor_name


class Medicine(models.Model):#药品信息表
    medicine_name = models.CharField(max_length=20)#药品名称
    medicine_num = models.IntegerField()#药品库存数量
    def __str__(self):
        return self.medicine_name

class User(models.Model):#用户表
    user_name = models.CharField(max_length=50)#用户名称
    user_passwd = models.CharField(max_length=20)#用户密码
    def __str__(self):
        return self.user_name