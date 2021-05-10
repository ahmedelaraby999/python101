class BasicPython:
    def __init__(self):
        self.help = ''' ທ່ານສາມາດໃຊ້ຄີເວີດ (Keyword) ດ້ານລຸ່ມ ເພື່ອສະແດງຄຳອະທິບາຍຕາມຫົວຂໍ້ທີ່ທ່ານສົນໃຈ ຕຢ. BasicPython.GetStart
        GetStart
        Syntax
        Comment
        Variable
        DataType
        Casting
        Condition
        WhileLoop
        ForLoop
        Function
        Lambda
        Class
        Inheritance
        Scope
        Module
        Pip
        TryExcept
        '''

        self.GetStart= 'Python ເປັນພາສາຄອມພິວເຕີ ທີ່ຈະເຮັດໃຫ້ທ່ານເຮັດວຽກໄດ້ໄວຂຶ້ນ ແລະ ນຳໃຊ້ລະບົບໄດ້ຢ່າງມີປະສິດທິພາບທີ່ສຸດ. ສາມາດສຶກສາເພີ່ມເຕີມໄດ້ຈາກລິ້ງ https://www.python.org'

        self.Syntax= 'Syntax ຫລື ໄວຍາກອນ - ພາສາ Python ເປັນພາສາທີ່ຄິດຄົ້ນມາໃຫ້ສາມາດຮຽນຮູ້ໄດ້ງ່າຍ\n ແມ່ນແຕ່ຜູ້ທີ່ບໍ່ເຄີຍຂຽນໂປຣແກຣມມາກ່ອນກໍ່ຕາມ,\n ໂດຍຫລັກໄວຍາກອນພື້ນຖານກໍ່ຈະແມ່ນການຫຍໍ້ໜ້າ (Indentation) ທີ່ສະແດງເຖິງຂອບເຂດການເຮັດວຽກ (Block) ຂອງງຊຸດຄຳສັ່ງນັ້ນໆ\nຕຢ. if a>b:\n\tprint("a>b")\nເຊິ່ງຫລັກການນຳໃຊ້ຫຍໍ້ໜ້າ ແມ່ນຈະໃຊ້ການ ຫຍະຫວ່າງ (Space) ຫລື Tab ຕາມຈຳນວນທີ່ເທົ່າກັນກໍ່ໄດ້ ແຕ່ຈະບໍ່ສາມາດໃຊ້ປົນກັນໄດ້.'

        self.Comment= 'Comment ຫລື ການບອກໃຫ້ Interpretor ບໍ່ສັ່ງໃຫ້ແຖວດັ່ງກ່າວເຮັດວຽກ, ສາມາດເຮັດໄດ້ດ້ວຍການໃຊ້ເຄື່ອງໝາຍ # ນຳໜ້າຊຸດຄຳສັ່ງດັ່ງກ່າວ\nຕຢ. # print("Hello World") ແຖວຊຸດຄຳສັ່ງດັ່ງກ່າວຈະບໍ່ເຮັດວຽກ'

        self.Variable= 'Variable ຫລື ຕົວແປ - ເຮັດໜ້າທີ່ບັນທຶກ ຫລື ຈັດເກັບຂໍ້ມູນປະເພດຕ່າງໆ ເພື່ອໃຊ້ອ້າງອີງໃນການຂຽນໂປຣແກຣມ\nການໃຊ້ງານຕົວແປໃນພາສາ Python ສາມາດປະກາດໄດ້ດ້ວຍການໃຊ້ເຄື່ອງໝາຍເທົ່າກັບ (=) ຂັ້ນກາງລະຫວ່າງຕົວແປ ແລະ ຊຸດຂໍ້ມູນ\nຕຢ. a = 1\n b = "ທ.ສົມສີ"\nທີ່ສຳຄັນ ຕົວແປໃນພາສາ Python ເປັນແບບ Case-sensitive ສະແດງວ່າຕົວພິມນ້ອຍ ແລະ ຕົວພິມໃຫຍ່ ມີຄ່າແຕກຕ່າງກັນ\nຕົວແປໃນພາສາ Python ບໍ່ສາມາດຂຶ້ນຕົ້ນດ້ວຍຢ່າງອື່ນນອກຈາກ ຕົວອັກສອນ (A-z), ຕົວເລກ (0-9) ຫລື _ (Underscore) ເທົ່ານັ້ນ'

        self.DataType= 'DataType ຫລື ຊະນິດຂອງຂໍ້ມູນ - ແຕ່ລະພາສາມີຊະນິດຂອງຂໍ້ມູນທີ່ແຕກຕ່າງກັນ, ພາສາ Python ເອງກໍ່ມີປະເພດຂອງຂໍ້ມູນທີ່ໃຊ້ຈັດເກັບຂໍ້ມູນປະເພດຕ່າງໆ ເຊັ່ນ: str (String - ປະເພດຂໍ້ຄວາມ), Int (Integer - ປະເພດຕົວເລກຈຳນວນເຕັມ), float (ປະເພດຕົວເລກຈຳນວນຈິງ), complex (ປະເພດຕົວເລກຊັບຂ້ອນ), lst (List - ຈັດເກັບເປັນລຳດັບ), tuple (Tuple - ຄ້າຍກັບ List ແຕ່ຈະບໍ່ສາມາດແກ້ໄຂຂໍ້ມູນໄດ້), dict (Dictionary - ຈັດເກັບດ້ວຍຮູບແບບ key-value), set (Set - ຄ້າຍກັບ List ແຕ່ຈະບໍ່ສາມາດເກັບຄ່າຊ້ຳຊ້ອນກັນໄດ້), bool (Boolean - ເປັນຄ່າທາງຕັກກະ ຖືກ - ຜິດ ຫລື True - False), bytes (ເກັບໃນຮູບແບບ Bytes), bytearray (ເກັບໃຊຮູບແບບ Bytearray), memoryview (ເກັບໃນຮູບແບບ Memoryview)\nເຊິ່ງສາມາດກວດສອບປະເພດຂອງຂໍ້ມູນໄດ້ດ້ວຍຄຳສັ່ງ type(ຕົວແປ) ເຊັ່ນ:\na = 1\nb="test"\ntype(a)\type(b)'

        self.Casting= 'Casting ຫລື ການກຳນົດປະເພດຂອງຂໍ້ມູນ ເຊັ່ນ: int(a) ຈະເປັນການປ່ຽນຕົວແປ a ໃຫ້ກາຍເປັນຂໍູມູນປະເພດຕົວເລກຈະນວນເຕັມ ແລະ ສາມາດໃຊ້ກັບ float() ຫລື str() ໄດ້ເຊັ່ນດຽວກັນ'

        self.Condition= 'Condition ຫລື ເງື່ອນໄຂການເຮັດວຽກຂອງໂປຣແກຣມ ໄດ້ແກ່: if - elif - else\nຕຢ.\nif a:\n\tprint("a")\nelif b:\n\tprint("b")\nelse:\n\tprint("else")\n ຊຸດຄຳສັ່ງດ້ານເທິງຈະສະແດງ a ຫາກເງື່ອນໄຂ a ເປັນຈິງ, ສະແດງ b ຫາກເງື່ອນໄຂ b ເປັນຈິງ ແລະ else ຫາກເງື່ອນໄຂອື່ນໆ ເປັນຈິງ ນອກເໜືອຈາກ a ແລະ b. ໂດຍຈະສັງເກດວ່າ else ບໍ່ຈຳເປັນຕ້ອງໃສ່ເງື່ອນໄຂໃດໆ ເພີ່ມ'

        self.WhileLoop= 'WhileLoop ເປັນການເຮັດຊ້ຳຈົນກວ່າເງື່ອນໄຂທີ່ວາງໄວ້ຈະເປັນຈິງ ເຊັ່ນ: ປ້ອນລະຫັດຜ່ານໃຫ້ຖືກຕ້ອງຈຶ່ງສາມາດເຂົ້າລະບົບໄດ້'

        self.ForLoop= 'ForLoop ເປັນການເຮັດຊ້ຳຕາມເງື່ອນໄຂທີ່ວາງໄວ້ ສ່ວນໃຫຍ່ຈະເປັນການເຮັດຊ້ຳເມື່ອມີຈຳນວນຮອບທີ່ແນ່ນອນ'

        self.Function= 'Function ໝາຍເຖິງກຸ່ມຄຳສັ່ງທີ່ຈະເຮັດວຽກເມື່ອຖືກເອີ້ນໃຊ້ງານ ແລະ ສາມາດເອີ້ນໃຊ້ໄດ້ຕາມຈຳນວນຄັ້ງທີ່ຕ້ອງການນ ໂດຍການຂຽນໂຄດພຽງຊຸດດຽວ'

        self.Lambda= 'Lambda ເປັນ Function ຮູບແບບໜຶ່ງ ທີ່ບໍ່ຈຳເປັນຕ້ອງປະກາດຊື່ ຫລື ເອີ້ນວ່າ Annonymous Function, ໃຊ້ກັບສົມຜົນງ່າຍໆ ຫລື ເງືອນໃຂທີ່ບໍ່ຊັບຊ້ອນ'

        self.Class= 'Class ເປັນຄຳທີ່ລະບຸເຖິງຮູບແບບການຂຽນໂຄດແບບ OOP (Object Oriented Programming) ທີ່ກຳລັງເປັນທີ່ນິຍົມ,\nໂດຍການສ້າງແບບ ຫລື ພິມຂຽວເພື່ອເປັນໂຄງສ້າງຫລັກ ແລະ ສາມາດສືບທອດຄຸນສົມບັດຕ່າງໆ ຂອງ Class ຕົ້ນແບບໄດ້.'

        self.Inheritance= 'Inheritance ໝາຍເຖິງການສືບທອດຄຸນສົມບັດຂອງ Class ຫລັກ ຫລື ຮູ້ຈັກກັນໃນນາມ Super Class'

        self.Scope= 'Scope ໝາຍເຖິງ ຂອບເຂດການເຂົ້າເຖິງຕົວແປພາຍໃນໂປຣແກຣມ ແບ່ງອອກເປັນສອງຂອບເຂດໄດ້ເກ່ Global (ເຂົ້າເຖິງໄດ້ຈາກທຸກສ່ວນຂອງໂປຣແກຣມ) ແລະ Local (ສາມາດເຂົ້າເຖິງພາຍໃນ Class ຫລື Function ນັ້ນໆ ເທົ່ານັ້ນ)'

        self.Module= 'Module ເປັນຊຸດຄຳສັ່ງ (ບາງຄົນອາດຮູ້ຈັກໃນຊື່ Library) ທີ່ແຍກອອກຈາກຊຸດຄຳສັ່ງຫລັກ ເພື່ອຄວາມງ່າຍໃນການຈັດການໂຄດ ຫລື ຄວາມສະດວກສະບາຍໃນການນຳຊຸດຄຳສັ່ງຂອງຜູ້ອື່ນມາໃຊ້ງານ'

        self.Pip= 'Pip ເປັນໂປຣແກຣມທີ່ຊ່ວຍໃຫ້ເຮົາສາມາດດາວໂຫລດ Package ທີ່ຄົນອື່ນສ້າງໄວ້ໃນ www.PyPi.org ໂດຍສາມາດຕິດຕັ້ງໄດ້ດ້ວຍຄຳສັ່ງ\npip install PACKAGENAME'

        self.TryExcept= 'TryExcept ເປັນການດັກຈັບ Error ໃນຂະນະທີ່ໂປຣແກຣມເຮັດວຽກ.'

# CLASS INHERITANCE
class Comment(BasicPython):
    def __init__(self):
        super().__init__()
        self.single = 'ການ Comment ໂຄດແຖວດຽວສາມາດເຮັດໄດ້ດ້ວຍການເພື່ອເຄື່ອງໝາຍ # ເຂົ້າໄປດ້ານໜ້າຂອງໂຄດແຖວດັ່ງກ່າວ'
        self.multiple = 'ການ Comment ໂຄດຫລາຍແຖວສາມາດເຮັດໄດ້ດ້ວຍການຂຽນໂຄດພາຍໃນ ””” ໂຄດພາຍໃນນີ້ຈະບໍ່ຖືກ Run ””” ເຊິ່ງສາມາດໃຊ້ໄດ້ທັງ Single Quote ຫລື Double Quote'


class PyPi101():
    def __init__(self):
        self.desc = 'Python Index Package'


if __name__ == '__main__':
    var1 = BasicPython()
    var2 = PyPi101()
    var3 = Comment()

    print(var1.GetStart)
    print('==================')
    print(var1.Syntax)
    print('==================')
    print(var1.Comment)
    print('==================')
    print(var1.Variable)
    print('==================')
    print(var1.DataType)
    print('==================')
    print(var1.Casting)
    print('==================')
    print(var1.Condition)
    print('==================')
    print(var1.WhileLoop)
    print('==================')
    print(var1.ForLoop)
    print('==================')
    print(var1.Function)
    print('==================')
    print(var1.Lambda)
    print('==================')
    print(var1.Class)
    print('==================')
    print(var1.Inheritance)
    print('==================')
    print(var1.Scope)
    print('==================')
    print(var1.Module)
    print('==================')
    print(var1.Pip)
    print('==================')
    print(var1.TryExcept)
    print('==================')
    print(var2.desc)
    print('==================')
    print(var3.single)
    print('==================')
    print(var3.multiple)
