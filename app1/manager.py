from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self,username,password,**kwargs):

        if not username:
            raise ValueError('Email is require')

        username=self.normalize_email(username)
        user=self.model(username=username,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self,username,password,**kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)
        kwargs.setdefault('is_active',True)



        if kwargs.get('is_staff') is not True:
            raise ValueError(('Super user must have is_staff true'))

        if kwargs.get('is_superuser') is not True:
            raise ValueError(('Super user must have is_superuser true'))

        if kwargs.get('is_active') is not True:
            raise ValueError(('Super user must have is_active true'))

        return self.create_user(username,password,**kwargs)