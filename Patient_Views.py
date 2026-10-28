from mysql import connector
import datetime
class dbconnect:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host = "localhost",
                user = "root",
                password = "Afreen@2004",
                database = "hospital_db"
            )
            return self.connection
        except Exception as e:
            return None
class PatientManager(dbconnect):
        def get_object(self,id= None):
            try:
                self.connect = super().get_connected()
                self.cursor = self.connection.cursor()
                query = "Select * from patient where id = %s"
                values = (id,)
                self.cursor.execute(query,values)
                record = self.cursor.fetchone()
                return record
            except Exception as e:
                return None
        def get(self):
            try:
                self.connect = super().get_connected()
                self.cursor = self.connection.cursor()
                query = "Select * from patient"
                self.cursor.execute(query)
                records = self.cursor.fetchall()
                return records
                # for data in records:
                #     print(data)
            except Exception as e:
                print(e)
        def post(self,**kwargs):
            try:
                self.connect = super().get_connected()
                self.cursor = self.connection.cursor()
                query = "insert into patient(Name,Age,Gender,Mobile,Disease,Doctor,Admission_date) values(%s,%s,%s,%s,%s,%s,%s)"
                values = [v for v in kwargs.values()]
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Patient added successfully...! ")
            except Exception as e:
                print(e)
        def retrieve(self,id=None):
            try:
                self.connect = super().get_connected()
                record = self.get_object(id = id)
                if record != None:
                    print(record)
                else:
                    print("Patient not found...!")
            except Exception as e:
                print(e)
        def put(self,id=None,**kwargs):
            try:
                self.connect = super().get_connected()
                record = self.get_object(id =id)
                if record != None:
                    placeholder = ""
                    for k in kwargs:
                        placeholder += k + "=%s,"
                    placeholder = placeholder.rstrip(",")
                    query = f"update patient set {placeholder} where id = %s"
                    values = [v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Patient details updated successfully...!")
                else:
                    print("Patient not found...!")
            except Exception as e:
                print(e)
        def delete(self,id = None):
            try:
                self.connect = super().get_connected()
                record = self.get_object(id = id)
                values = (id,)
                if record != None:
                    self.cursor = self.connection.cursor()
                    query = "delete from patient where id =%s"
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Patient details deleted successfully...!")
                else:
                    print("Patient not found...!")
            except Exception as e:
                print(e)



# connection_instance = dbconnect()
# print(connection_instance.get_connected())
# patient_instance =PatientManager()
# patient_instance.get()
# # patient_instance.post(Name = "Arun",Age =28,Gender = "Male",Mobile =9890876213,Disease= "Stomachache",Doctor = "Remya",Admission_date =datetime.datetime.today())
# print("_ _ _ _ Details of one patient _ _ _ _")
# patient_instance.retrieve(2)
# print("_ _ _ _ Updation _ _ _ _")
# patient_instance.put(3,Doctor = "Akhila")
# print("_ _ _ _ Deletion _ _ _ _")
# patient_instance.delete(4)