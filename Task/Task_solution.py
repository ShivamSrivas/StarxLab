#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Task:#Created a class named as [Task]
    def Customer(self,a,b):#created a method
        """
        Write a function which takes two arguments: a list of customers and the number of open cash registers. Each customer is represented by an integer which indicates the amount of time needed to checkout. Assuming that customers are served in their original order, your function should output the minimum time required to serve all customers.
        Example:
        get_checkout_time([5, 1, 3], 1) should return 9
        get_checkout_time([10, 3, 4, 2], 2) should return 10 because while the first register is busy serving customer[0] the second register can serve all remaining customers.
        """
        customer=a
        reg=b
        Worst_time=0
        local=0
        if b==1:
            for i in a:
                Worst_time+=i
            return Worst_time
        else:
            ma=max(customer)
            customer.pop(customer.index(ma))
            for i in customer:
                local+=i
            if local<=ma:
                return ma
            else:
                return ma+min(customer)
    def String_Function(self,a):#Created a Method named as "String_Function" to fulfill the giving condition
        """
        Condition:
        Return true if the string in the first element of the list contains all of the letters of the string in the second element of the
        list.
        examples
        ["hello", "Hello"]
        should return true because all of the letters in the second string are present in the first, ignoring case.
        ["hello", "hey"]
        should return false because the string "hello" does not contain a "y".
        ["Alien", "line"]
        should return true because all of the letters in "line" are present in "Alien".
        
        Parameter:Takes list as arguements
        
        """
        try:
            count=True
            first=str.lower(a[0])#Since there was no condition for lower and upper case,I converted both of them in lower case
            second=str.lower(a[1])#Doing same here
            for i in second:#Iterating one by one in second element['String'] in list
                if i in first:#Checking the condition
                    count=count*True#If true then multiply with "True"
                else:
                    count=count*False#Else multiply with false
            return bool(count)#If Statisy all condition then return True else False
        except Exception as e:
            print(str(e))


# In[ ]:




