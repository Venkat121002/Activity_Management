from django.db import models

# Create your models here.
class Task(models.Model):
    RELATED_CHOICES = [
        ('Lead','Lead'),
        ('Customer','Customer'),
        ('Deal','Deal'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'), 
        ('In Progress', 'In Progress'), 
        ('Completed', 'Completed'), 
        ('Cancelled', 'Cancelled'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'), 
        ('Medium','Medium'), 
        ('High', 'High'),
    ]

    task_id = models.CharField(max_length=20,unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    related_to_type = models.CharField(max_length=50,choices=RELATED_CHOICES)
    related_to_id = models.PositiveIntegerField()
    assigned_to = models.CharField(max_length=255)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    start_date = models.DateField(blank=True,null=True)
    due_date = models.DateField(blank=True,null=True)
    completed_date = models.DateField(blank=True,null=True)
    remarks = models.TextField(blank=True,null=True)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class ActivityLog(models.Model):
    
    ACTIONTYPE_CHOICES = [
        ('Comment', 'Comment'),
        ('Status Update', 'Status Update'), 
        ('Follow up', 'Follow up'), 
        ('Reminder', 'Reminder'),
    ]

    activity_id = models.CharField(max_length=20,unique=True)
    task = models.ForeignKey('Task',on_delete=models.CASCADE,related_name='activities')
    action_type = models.CharField(max_length=100,choices=ACTIONTYPE_CHOICES)
    note = models.TextField()
    performed_by = models.CharField(max_length=255)
    performed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
    
class Remainder(models.Model):

    remainder_id = models.CharField(max_length=20, unique=True)
    task = models.ForeignKey('Task',on_delete=models.CASCADE,related_name='reminders')
    reminder_date = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
    


