class FacebookDataDelete(TimeStampedModel):
    STATUS = (
        ('completed', 'completed'),
        ('initiated', 'initiated')
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey('users.User', default=None, blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return f'{self.user.email} status: {self.status}'
    
class CheckUserDeletionStatus(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        try:
            f_del=FacebookDataDelete.objects.get(uuid=request.GET.get('user'))
            return HttpResponse(f'Your data deletion process is {f_del.status}')
        except :
            return HttpResponse(f'Invalid Request')
