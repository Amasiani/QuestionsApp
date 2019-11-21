from django.db import models



class School(models.Model):

    SCHOOL_NAME = (
        ('AAU',  'Ambrose Alli University, Ekpoma'),
        ('AAUA',  'Adekunle Ajasin University, Akungba'),
        ('ABSU',   'Abia State University, Uturu'),
        ('ADSU',  'Adamawa State University Mubi'),
        ('AKSU',  'Akwa Ibom State University of Technology, Uyo'),
        ('BASUG',  'Bauchi State University, Gadau'),
        ('BMU',  'Bayelsa Medical University'),
        ('BOSU',  'Bornu State University, Maiduguri'),
        ('COOU',  'Chukwuemeka Odumegwu Ojukwu University, Uli'),
        ('CRUTECH',  'Cross River State University of Science and Technology, Calabar'),
        ('DELSU',  'Delta State University Abraka'),
        ('EBSU',  'Ebonyi State University, Abakaliki'),
        ('EKSU',  'Ekiti State University, Ekiti'),
        ('EPU',  'Eastern Palm University Ogboko, Imo State'),
        ('ESUT',  'Enugu State University of Science and Technology, Enugu'),
        ('EUI',  'Edo University Iyamo'),
        ('GSU',  'Gombe State Univeristy, Gombe'),
        ('GUST',  'Gombe State University of Science and Technology'),
        ('IAUE',  'Ignatius Ajuru University of Education, Rumuolumeni'),
        ('IBBU',  'Ibrahim Badamasi Babangida University, Lapai'),
        ('IMSU',  'Imo State University, Owerri'),
        ('KASU',  'Kaduna State University, Kaduna'),
        ('KSU',  'Kogi State University Anyigba'),
        ('KSUST',  'Kebbi State University, Kebbi'),
        ('KUST',  'Kano University of Science & Technology, Wudil'),
        ('KWASU',  'Kwara State University, Ilorin'),
        ('LASU',  'Lagos State University, Ojo'),
        ('LAUTECH',  'Ladoke Akintola University of Technology, Ogbomoso'),
        ('MUSTA',  'Moshood Abiola University of Science and Technology Abeokuta'),
        ('NDU',  'Niger Delta University Yenagoa'),
        ('NSUK',  'Nasarawa State University Keffi'),
        ('NWU',  'Northwest University Kano'),
        ('OOU',  'Olabisi Onabanjo University, Ago Iwoye'),
        ('OSUSTECH',  'Ondo State University of Science and Technology Okitipupa'),
        ('PLASU',  'Plateau State University Bokkos'),
        ('RSUST',  'River State University of Science and Technology'),
        ('SLU',  'Sule Lamido University, Kafin Hausa, Jigawa'),
        ('SSU',  'Sokoto State University'),
        ('TASU',  'Taraba State University, Jalingo'),
        ('TASUED',  'Tai Solarin University of Education Ijebu Ode'),
        ('Tech-U',  'Oyo State Technical University Ibadan'),
        ('UAT',  'University of Africa Toru Orua, Bayelsa State'),
        ('UMYU',  'Umar Musa Yar’ Adua University Katsina'),
        ('UNIMED',  'Ondo State University of Medical Sciences'),
        ('UNIOSUN',  'Osun State University Osogbo'),
        ('YSU',  'Yobe State University, Damaturu'),
        ('ZSU',  'Zamfara State University'),
        ('ABU', 'Ahmadu Bello University, Zaria	 Courses'),
        ('AFIT', 'Air Force Institute of Technology, Kaduna'),
        ('ATBU', 'Abubakar Tafawa Balewa University, Bauchi'),
        ('BSU',  'Benue State University, Makurdi'),
        ('BUK', 'Bayero University, Kano'),
        ('FUAM', 'University of Agriculture, Makurdi'),
        ('FUBK', 'Federal University, Birnin Kebbi'),
        ('FUD', 'Federal University, Dutse, Jigawa State'),
        ('FUDMA', 'Federal University, Dutsin-Ma, Katsina'),
        ('FUGASHUA', 'Federal University Gashua, Yobe'),
        ('FUGUS', 'Federal University, Gusau Zamfara'),
        ('FUKASHERE', 'Federal University, Kashere, Gombe State'),
        ('FULAFIA', 'Federal University, Lafia, Nasarawa State'),
        ('FULOKOJA', 'Federal University, Lokoja, Kogi State'),
        ('FUNAAB', 'Federal University of Agriculture, Abeokuta'),
        ('FUNAI', 'Federal University, Ndifu-Alike, Ebonyi State'),
        ('FUOTUOKE', 'Federal University, Otuoke, Bayelsa'),
        ('FUOYE', 'Federal University, Oye-Ekiti, Ekiti State'),
        ('FUPRE', 'Federal University of Petroleum Resources, Effurun'),
        ('FUTA', 'Federal University of Technology, Akure'),
        ('FUTMINNA', 'Federal University of Technology, Minna'),
        ('FUTO', 'Federal University of Technology, Owerri'),
        ('FUWUKARI', 'Federal University, Wukari, Taraba State'),
        ('MAUTECH', 'odibbo Adama University of Technology, Yola'),
        ('MOUAU', 'Michael Okpara University of Agricultural Umudike'),
        ('NAUB', 'Nigerian Army University BiU'),
        ('NDA', 'Nigerian Defence Academy Kaduna'),
        ('NMU', 'Nigerian Maritime University Okerenkoko, Delta State'),
        ('NOUN', 'National Open University of Nigeria, Lagos'),
        ('NPA', 'Nigeria Police Academy Wudil'),
        ('OAU', 'Obafemi Awolowo University, Ile-Ife'),
        ('UDUSOK', 'Usumanu Danfodiyo University'),
        ('UI', 'University of Ibadan'),
        ('UNIABUJA', 'University of Abuja, Gwagwalada'),
        ('UNIBEN', 'University of Benin'),
        ('UNICAL', 'University of Calabar'),
        ('UNIJOS', 'University of Jos'),
        ('UNILAG', 'University of Lagos'),
        ('UNILORIN', 'University of Ilorin'),
        ('UNIMAID',   'University of Maiduguri'),
        ('UNIPORT', 'University of Port-Harcourt'),
        ('UNIUYO', 'University of Uyo'),
        ('UNIZIK', 'Nnamdi Azikiwe University, Awka'),
        ('UNN',	'University of Nigeria, Nsukka'),

    )
    name = models.CharField(max_length=10, choices=SCHOOL_NAME)
   

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name


class Question(models.Model):
    course_code     = models.CharField(max_length=50)
    session         = models.DateField()
    semester        = models.SmallIntegerField()    
    image           = models.FileField(upload_to='uploads/')
    school          = models.ForeignKey(School, on_delete=models.CASCADE)
    department      = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_code
