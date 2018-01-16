USER_IDENTITY_UNSET = -1
USER_IDENTITY_SUPERADMIN = 0
USER_IDENTITY_ADMIN = 1
USER_IDENTITY_TEACHER = 2
USER_IDENTITY_STUDENT = 3
USER_IDENTITIES = (
    (USER_IDENTITY_SUPERADMIN, '超级管理员'),
    (USER_IDENTITY_ADMIN, '平台管理员'),
    (USER_IDENTITY_TEACHER, '教师'),
    (USER_IDENTITY_STUDENT, '学生'),
)
REGISTER_IDENTITIES = (
    (USER_IDENTITY_STUDENT, '学生'),
)

INSTITUTES = (
    ('0000', '其他'),
    ('0101', '化工学院'),
    ('0102', '化学学院'),
    ('0103', '环境学院'),
    ('0104', '生命科学与技术学院'),
    ('0105', '化工机械学院'),
    ('0106', '制药科学与技术学院'),
    ('0107', '精细化工国家重点实验室'),
    ('0201', '电气工程学院'),
    ('0202', '电子科学与技术学院'),
    ('0203', '半导体技术学院'),
    ('0204', '信息与通信工程学院'),
    ('0205', '控制科学与工程学院'),
    ('0206', '计算机科学与技术学院'),
    ('0207', '生物医学工程系'),
    ('0208', '计算机基础实验教学中心'),
    ('0301', '水利工程学院'),
    ('0302', '土木工程学院'),
    ('0303', '交通运输学院'),
    ('0304', '工程管理系'),
    ('0401', '工程力学系'),
    ('0402', '船舶工程学院'),
    ('0403', '汽车工程学院'),
    ('0404', '航空航天学院'),
    ('0501', '机械工程学院'),
    ('0502', '材料科学与工程学院'),
    ('0503', '能源与动力学院'),
    ('0601', '管理科学与工程学院'),
    ('0602', '工商管理学院'),
    ('0603', '经济学院'),
    ('0604', 'MBA教育中心/EMBA中心'),
    ('0701', '人文学院'),
    ('0702', '公共管理与法学学院'),
    ('0703', '马克思主义学院'),
    ('0704', 'MPA教育中心'),
    ('0801', '建筑系'),
    ('0802', '城市规划系'),
    ('0803', '艺术系'),
    ('0804', '工业设计系'),
    ('0901', '嵌入式系统工程系'),
    ('0902', '服务科学与工程系'),
    ('0903', '数字媒体技术系'),
    ('0904', '软件工程系'),
    ('0905', '网络工程系'),
    ('1000', '外国语学院'),
    ('1100', '物理与光电工程学院'),
    ('1200', '数学科学学院'),
    ('1300', '体育教学部'),
    ('1400', '国际文化交流学院'),
    ('1500', '国防教育学院'),
    ('1600', '创新创业学院'),
    ('1700', '城市学院'),
    ('1800', '继续教育学院'),
    ('1900', '机关'),
    ('2000', '校医院'),
    ('9801', '石油与化学工程学院'),
    ('9802', '食品与环境学院'),
    ('9803', '生命与医药学院'),
    ('9804', '文法学院'),
    ('9805', '商学院'),
    ('9806', '海洋科学与技术学院'),
    ('9807', '基础教学部'),
)
EDUCATION_NONE = -1
EDUCATION_UNDERGRADUATE_1 = 1
EDUCATION_UNDERGRADUATE_2 = 2
EDUCATION_UNDERGRADUATE_3 = 3
EDUCATION_UNDERGRADUATE_4 = 4
EDUCATION_POSTGRADUATE = 5

EDUCATION_BACK = (
    (EDUCATION_NONE, '其他'),
    (EDUCATION_UNDERGRADUATE_1, '本科一年级'),
    (EDUCATION_UNDERGRADUATE_2, '本科二年级'),
    (EDUCATION_UNDERGRADUATE_3, '本科三年级'),
    (EDUCATION_UNDERGRADUATE_4, '本科四年级'),
    (EDUCATION_POSTGRADUATE, '研究生'),
)

TEACHER_ENGINEER = 0
TEACHER_SENGINEER = 1
TEACHER_LECTURER = 2
TEACHER_APROF = 3
TEACHER_PROF = 4
TEACHER_TITLE = (
    (TEACHER_ENGINEER, '工程师'),
    (TEACHER_SENGINEER, '高级工程师'),
    (TEACHER_LECTURER, '讲师'),
    (TEACHER_APROF, '副教授'),
    (TEACHER_PROF, '教授'),
)
