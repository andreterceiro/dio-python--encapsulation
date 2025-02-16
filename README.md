# General

Definition of encapsulation:

![Definition](images/definition.png)

Teacher enforced that there is a convention to not access private or protected methods, not a keyword to make the enforcement. I [talked to ChatGPT](https://chatgpt.com/c/67b20ee4-f844-8007-ba73-b8d23f97b725) to explore more the question.

Please see this test:

```python
class Account:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute
        self.__batata = 1
        self._cebola = 1
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, value):
        if value > 0:
            self.__balance += value
            return True
        return False
    
    def withdraw(self, value):
        if 0 < value <= self.__balance:
            self.__balance -= value
            return True
        return False

# Example usage:
account = Account(100)
account.deposit(50)
print(account.balance)  # 150
account.withdraw(30)
print(account.balance)  # 120
# print(account.__batata) 2 underlines => error
print(account._cebola) # 1 underline => ok
```

ChatGPT confirmed the information of the convention passed by the teacher, but passed a better alternative: the use of two underlines before the name of the property. As you can see in the example, we cannot access outside of the class a property who name starts with two underlines. 


# Talking about property

![property](images/property.png)

Please see this interesting example of the teacher. He inserted in the code `@property` and also `@x.setter` and `@x.deleter`:

![property example](images/property-example.png)

As you could see in the examples, if you use `@property` you will access the property **without** parentheses.

If you do not define in the example `@x.setter`, you will can't set the x value (using "foo.x = 10" as example).

Teacher said that to `@x.deleter` in the example we can use del, but this is not interesting (use `del` can result in errors in other parts of the code that depends on this property), so he prefered to use `self._x = -1`.

![using del](images/using-del.png)


# Slides of the class

[link](https://academiapme-my.sharepoint.com/:p:/g/personal/nubia_dio_me/EQT6XJxrBjFGs_OWHrHasOgBQl5FC3wqBPbHEOtlo5eIdQ?e=gmVfaM)



# Repository related to the classes

[link](https://github.com/digitalinnovationone/trilha-python-dio)