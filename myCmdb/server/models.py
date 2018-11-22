from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Server_info(models.Model):
    '''
    服务器的基本信息
    '''
    ip=models.CharField(max_length=32,verbose_name='服务器IP')
    mac=models.CharField(max_length=32,verbose_name='服务器物理地址')
    cpu=models.CharField(max_length=32,verbose_name='服务器cpu')
    memory=models.CharField(max_length=32,verbose_name='服务器内存')
    disk=models.CharField(max_length=32,verbose_name='服务器硬盘')
    isalive=models.CharField(max_length=32,verbose_name='服务器状态')

#可以使用命令：
#cat /proc/cpuinfo |awk -F: '{print $1}'|sed 's/ /_/'
class Cpu_info(models.Model):
    processor = models.CharField(max_length=32,blank=True,null=True)
    vendor_id = models.CharField(max_length=32,blank=True,null=True)
    cpu_family = models.CharField(max_length=32,blank=True,null=True)
    model = models.CharField(max_length=32,blank=True,null=True)
    model_name = models.CharField(max_length=32,blank=True,null=True)
    stepping = models.CharField(max_length=32,blank=True,null=True)
    microcode = models.CharField(max_length=32,blank=True,null=True)
    cpu_MHz = models.CharField(max_length=32,blank=True,null=True)
    cache_size = models.CharField(max_length=32,blank=True,null=True)
    physical_id = models.CharField(max_length=32,blank=True,null=True)
    siblings = models.CharField(max_length=32,blank=True,null=True)
    core_id = models.CharField(max_length=32,blank=True,null=True)
    cpu_cores = models.CharField(max_length=32,blank=True,null=True)
    apicid = models.CharField(max_length=32,blank=True,null=True)
    initial_apicid = models.CharField(max_length=32,blank=True,null=True)
    fpu = models.CharField(max_length=32,blank=True,null=True)
    fpu_exception = models.CharField(max_length=32,blank=True,null=True)
    cpuid_level = models.CharField(max_length=32,blank=True,null=True)
    wp = models.CharField(max_length=32,blank=True,null=True)
    flags = models.CharField(max_length=32,blank=True,null=True)
    bogomips = models.CharField(max_length=32,blank=True,null=True)
    clflush_size = models.CharField(max_length=32,blank=True,null=True)
    cache_alignment = models.CharField(max_length=32,blank=True,null=True)
    address_sizes = models.CharField(max_length=32,blank=True,null=True)
    power_management = models.CharField(max_length=32,blank=True,null=True)

class Memory_info(models.Model):
    MemTotal = models.CharField(max_length=32, blank=True, null=True)
    MemFree = models.CharField(max_length=32, blank=True, null=True)
    MemAvailable = models.CharField(max_length=32, blank=True, null=True)
    Buffers = models.CharField(max_length=32, blank=True, null=True)
    Cached = models.CharField(max_length=32, blank=True, null=True)
    SwapCached = models.CharField(max_length=32, blank=True, null=True)
    Active = models.CharField(max_length=32, blank=True, null=True)
    Inactive = models.CharField(max_length=32, blank=True, null=True)
    Active_anon = models.CharField(max_length=32, blank=True, null=True)
    Inactive_anon = models.CharField(max_length=32, blank=True, null=True)
    Active_file = models.CharField(max_length=32, blank=True, null=True)
    Inactive_file = models.CharField(max_length=32, blank=True, null=True)
    Unevictable = models.CharField(max_length=32, blank=True, null=True)
    Mlocked = models.CharField(max_length=32, blank=True, null=True)
    SwapTotal = models.CharField(max_length=32, blank=True, null=True)
    SwapFree = models.CharField(max_length=32, blank=True, null=True)
    Dirty = models.CharField(max_length=32, blank=True, null=True)
    Writeback = models.CharField(max_length=32, blank=True, null=True)
    AnonPages = models.CharField(max_length=32, blank=True, null=True)
    Mapped = models.CharField(max_length=32, blank=True, null=True)
    Shmem = models.CharField(max_length=32, blank=True, null=True)
    Slab = models.CharField(max_length=32, blank=True, null=True)
    SReclaimable = models.CharField(max_length=32, blank=True, null=True)
    SUnreclaim = models.CharField(max_length=32, blank=True, null=True)
    KernelStack = models.CharField(max_length=32, blank=True, null=True)
    PageTables = models.CharField(max_length=32, blank=True, null=True)
    NFS_Unstable = models.CharField(max_length=32, blank=True, null=True)
    Bounce = models.CharField(max_length=32, blank=True, null=True)
    WritebackTmp = models.CharField(max_length=32, blank=True, null=True)
    CommitLimit = models.CharField(max_length=32, blank=True, null=True)
    Committed_AS = models.CharField(max_length=32, blank=True, null=True)
    VmallocTotal = models.CharField(max_length=32, blank=True, null=True)
    VmallocUsed = models.CharField(max_length=32, blank=True, null=True)
    VmallocChunk = models.CharField(max_length=32, blank=True, null=True)
    HardwareCorrupted = models.CharField(max_length=32, blank=True, null=True)
    AnonHugePages = models.CharField(max_length=32, blank=True, null=True)
    HugePages_Total = models.CharField(max_length=32, blank=True, null=True)
    HugePages_Free = models.CharField(max_length=32, blank=True, null=True)
    HugePages_Rsvd = models.CharField(max_length=32, blank=True, null=True)
    HugePages_Surp = models.CharField(max_length=32, blank=True, null=True)
    Hugepagesize = models.CharField(max_length=32, blank=True, null=True)
    DirectMap4k = models.CharField(max_length=32, blank=True, null=True)
    DirectMap2M = models.CharField(max_length=32, blank=True, null=True)
    DirectMap1G = models.CharField(max_length=32, blank=True, null=True)


class Server_cpu(models.Model):
    '''
    服务器关联cpu
    '''
    server_id = models.IntegerField()
    cpu_id= models.IntegerField()


class server_memory(models.Model):
    server_id = models.IntegerField()
    memory_id = models.IntegerField()

class CMDBUser(models.Model):


    username=models.CharField(max_length=32,verbose_name='用户账号')
    password=models.CharField(max_length=32,verbose_name='用户密码')
    nickname=models.CharField(max_length=32,verbose_name='用户姓名')
    phone=models.CharField(max_length=32,verbose_name='用户手机号')
    email=models.EmailField(max_length=32,verbose_name='用户邮箱')
    photo=models.ImageField(max_length=32,verbose_name='用户头像',upload_to='images')
    service=models.ManyToManyField(Server_info)

class api_info(models.Model):
    name = models.CharField(max_length=32,verbose_name='接口名称')
    description = RichTextUploadingField(verbose_name='接口描述')
    doc = models.CharField(max_length=64,verbose_name='接口说明')



class Service(models.Model):
    '''
    服务器
    '''
    ip = models.CharField(max_length=32,verbose_name='服务器IP')
    mac = models.CharField(max_length=32,verbose_name='服务器MAC')
    cpu = models.CharField(max_length=32,verbose_name='服务器CPU')
    memory = models.CharField(max_length=32,verbose_name='服务器内存P')
    hostname = models.CharField(max_length=32,verbose_name='服务器主机')
    isalive = models.CharField(max_length=32,verbose_name='服务器状态')

    def __str__(self):
        return self.ip

class APITonken(models.Model):
    '''
    服务器
    '''
    value = models.CharField(max_length=32,verbose_name='token值')
    #这里一定要注意Django setting默认设置的时间
    time = models.DateTimeField(max_length=32,verbose_name='生成时间')
    user_id = models.CharField(max_length=32,verbose_name='token用户')

    def __str__(self):
        return self.value