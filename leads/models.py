from django.db import models



class Lead(models.Model):
    contact = models.ForeignKey(Contact, related_name='leads', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Closed', 'Closed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.contact.name} - {self.status}'
