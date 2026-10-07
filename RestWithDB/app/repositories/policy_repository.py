from app.models.policy import Policy
from app.core.config import getconnection

class PolicyRepository:

    def get_all(self):
        connection=getconnection()
        cursor=connection.cursor()

        cursor.execute("select * from policies")

        rows=cursor.fetchall()
        cursor.close()
        connection.close()

        policies=[]
        for row in rows:
            policy=Policy(id=row[0],policy_number=row[1], name=row[2], description=row[3],maturity=row[4],premium=row[5],policy_type=row[6])
            policies.append(policy)

        return policies
    
    def get_by_id(self, p_id: int):
        connection = getconnection()
        cursor=connection.cursor()
        
        cursor.execute("select * from policies where id = %s",(p_id,))
        
        row=cursor.fetchone()
        cursor.close()
        connection.close()
        
        policy=Policy(id=row[0],policy_number=row[1], name=row[2], description=row[3],maturity=row[4],premium=row[5],policy_type=row[6])
        return policy
    
    def add_policy(self, policy: Policy):
        connection = getconnection()
        cursor=connection.cursor()
        
        cursor.execute("INSERT INTO policies(policy_number, name, description, maturity_years, premium, policy_type)VALUES (%s, %s, %s, %s, %s, %s)",(policy.policy_number, policy.name, policy.description, policy.maturity, policy.premium, policy.policy_type,))
        
        connection.commit()
        id=cursor.lastrowid
        
        cursor.close()
        connection.close()
        
        return id
    
    def update_policy(self,id:int, policy: Policy):
        connection=getconnection()
        cursor=connection.cursor()
        
        cursor.execute("""UPDATE policies SET policy_number = %s, name = %s, description = %s, maturity_years = %s, premium = %s, policy_type = %s WHERE id = %s """,( policy.policy_number, policy.name, policy.description,policy.maturity, policy.premium,policy.policy_type,id))    
        
        connection.commit()
        connection.close()
        
        return self.get_by_id(id)
        
        
        
    def remove_policy(self, p_id: int):
        connection = getconnection()
        cursor=connection.cursor()
        
        cursor.execute("delete from policies where id = %s",(p_id,))
        
        connection.commit()
        
        deleted = cursor.rowcount>0
        
        cursor.close()
        connection.close()
        
        return deleted