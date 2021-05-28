import json

senior = {
    "ccc": [{"name": "Mayank Sharma", "roll": "010", "type": "Chairman", "github":"https://github.com/mayanknimcet188", "linkedin":"https://www.linkedin.com/in/mayank-sharma-57414b198/"}],
    "eec": [{"name": "Kuldeep Patidar", "roll": "011", "type": "Chairperson", "github":"https://github.com/kuldeeppatidar47kp", "linkedin":"https://www.linkedin.com/in/kuldeep-patidar-4870751b4"}],
    "prc": [{"name": "Surbhi Dabhade", "roll": "012", "type": "Chairperson", "github":"https://github.com/surbhidabhade", "linkedin":"https://www.linkedin.com/in/surbhi-dabhade-bb711319b/"}],
    "ppc": [{"name": "Anand Prakash", "roll": "013", "type": "Chairperson", "github":"https://github.com/a4anandprakash", "linkedin":"https://www.linkedin.com/in/a4anandprakash"}],
    "arc": [{"name": "Mahima Pandey", "roll": "014", "type": "Chairperson", "github":"https://github.com/mahii99p", "linkedin":"https://www.linkedin.com/in/mahima-pandey-a58abb1a1"}],
    "rc": [{"name": "Mahima Pandey", "roll": "014", "type": "Chairperson", "github":"https://github.com/mahii99p", "linkedin":"https://www.linkedin.com/in/mahima-pandey-a58abb1a1"}]
    
}

junior_head = {
    "ccc": [
        {"name": "Bhumika Khakha", "roll": "024", "type": "Secretary", "github":"https://github.com/bhumikakhakha", "linkedin":"http://linkedin.com/in/bhumikakhakha"},
        {"name": "Shivam Dubey", "roll": "097", "type": "Treasurer", "github":"https://github.com/stech0703", "linkedin":"https://www.linkedin.com/in/shivam-dubey-862086203/"}
    ],
    "eec": [
        {"name": "Nikita Das", "roll": "062", "type": "Web Team", "github":"https://github.com/nikki-99", "linkedin":"https://www.linkedin.com/in/nikita-das-517085203/"},
        {"name": "Amit Kumar", "roll": "015", "type": "Web Team", "github":"https://github.com/015amit", "linkedin":"https://www.linkedin.com/in/amit015/"},
        {"name": "Anshu Mala Lakra", "roll": "019", "type": "Web Team", "github":"https://github.com/019anshu", "linkedin":"www.linkedin.com/in/019anshu"}
    ],
    "prc": 0,
    "ppc": 0,
    "arc": 0,
    "rc":0
}

data = {
    "ccc": [
        
            {"name": "Akriti Upadhyay", "roll": "007", "github":"https://github.com/akriti-upadhyay", "linkedin":"https://www.linkedin.com/in/akriti-upadhyay/"},
            {"name": "Amandeep Yadav", "roll": "010", "github":"https://github.com/appy79", "linkedin":"https://www.linkedin.com/in/010amandeep/"},
            {"name": "Himanshu Ghorwal", "roll": "035", "github":"https://github.com/zimanshu", "linkedin":"https://www.linkedin.com/in/himanshughorwal/"},
            {"name": "Mahima Pawar", "roll": "047", "github":"https://github.com/047-Mahima", "linkedin":"https://www.linkedin.com/in/mahima-pawar-8b7437178"},
            {"name": "Naman Tripathi", "roll": "054", "github":"https://github.com/054naman", "linkedin":"linkedin.com/in/naman-tripathi"},
            {"name": "Shivangi Gupta", "roll": "112", "github":"https://github.com/Shivangi112", "linkedin":"https://www.linkedin.com/in/shivangi-gupta-1138b4203/"}
        
    ],
    "eec": [
        {"name": "Aayushi", "roll": "002", "github":"https://github.com/aayushi-aqua", "linkedin":"https://www.linkedin.com/in/aayushi--singh/"},
        {"name": "Amitabha Roy", "roll": "013", "github":"https://github.com/Concept606", "linkedin":"https://www.linkedin.com/in/royamitabha/"},
        {"name": "Ankit Singh", "roll": "018", "github":"https://github.com/ankitsingh860", "linkedin":"https://www.linkedin.com/in/ankitsingh860/"},
        {"name": "Charu Bajaj", "roll": "026", "github":"github.com/CharuBajaj", "linkedin":"https://www.linkedin.com/mwlite/in/charu-bajaj-2888b4203"},
        {"name": "Deepeeka", "roll": "027", "github":"https://github.com/deepeekachudasama027", "linkedin":"https://www.linkedin.com/in/deepeekachudasama/"},
        {"name": "Dimple Gyanani", "roll": "028", "github":"https://github.com/028-Dimple", "linkedin":"www.linkedin.com/in/028-dimple"},
        {"name": "Harshit Omar", "roll": "031", "github":"", "linkedin":""},
        {"name": "Harsh Rai", "roll": "032", "github":"https://github.com/harshrai654", "linkedin":"www.linkedin.com/in/harsh-rai-a03a5a106"},
        {"name": "Himanshi Bansal", "roll": "034", "github":"https://github.com/himanshibansal-034", "linkedin":"www.linkedin.com/in/himanshi-bansal-2ba08a203"},
        {"name": "Hrishikant Mehta", "roll": "036", "github":"https://github.com/hrishikantmehta", "linkedin":"https://www.linkedin.com/in/hrishikantmehta/"},
        {"name": "Jasbir Sikhawat", "roll": "037", "github":"https://github.com/JasbirCodeSpace", "linkedin":"https://www.linkedin.com/in/jasbir-shikhawat"},
        {"name": "Manish Kumar Pandey", "roll": "049", "github":"https://github.com/mnk-q", "linkedin":"https://www.linkedin.com/in/mnk-q"},
        {"name": "Manish Nangliya", "roll": "050", "github":"https://github.com/manishnangliya", "linkedin":"https://www.linkedin.com/in/manishnangliya/"},
        {"name": "Pankaj Sharma", "roll": "068", "github":"https://github.com/pankajsharma068", "linkedin":"https://www.linkedin.com/in/pankaj-sharma-a2b35a200"},
        {"name": "Paras Tiwari", "roll": "069", "github":"https://github.com/ptiw-rep", "linkedin":"https://www.linkedin.com/in/tparas/"},
        {"name": "Payal Soni", "roll": "070", "github":"https://github.com/payalsoni-07", "linkedin":"https://www.linkedin.com/in/payal-soni-a57a991b2"},
        {"name": "Piyush Devda", "roll": "071", "github":"https://github.com/piyussh22", "linkedin":"https://www.linkedin.com/in/piyushdevda03"},
        {"name": "Sachin Lalwani", "roll": "084", "github":"https://github.com/084-sachin/", "linkedin":"https://www.linkedin.com/in/084-sachin/"},
        {"name": "Sachin Sharma", "roll": "085", "github":"https://github.com/sachin3045/", "linkedin":"https://www.linkedin.com/in/sachin3045/"},
        {"name": "Saurabh Anand", "roll": "092", "github":"https://github.com/anandsaurabh46", "linkedin":"https://www.linkedin.com/in/anandsaurabh46/"},
        {"name": "Shanoor Ahmed", "roll": "094", "github":"https://github.com/shanoorahmed", "linkedin":"https://www.linkedin.com/in/shanoorahmed/"},
        {"name": "Shobit Samaria", "roll": "099", "github":"https://github.com/shobhit099", "linkedin":"https://www.linkedin.com/mwlite/in/shobhit-samaria-1a484a202"},
        {"name": "Simran Garg", "roll": "103", "github":"https://github.com/Simran0501", "linkedin":"https://www.linkedin.com/in/simran-garg-0501"},
        {"name": "Sonu Gupta", "roll": "104", "github":"https://github.com/104-sonu-gupta", "linkedin":"https://www.linkedin.com/in/104-sonu-gupta/"},
        {"name": "Yasser Osman Khan", "roll": "110", "github":"https://github.com/yasserkhan45", "linkedin":"https://www.linkedin.com/in/yasserkhan45/"},
        {"name": "Suruchi Bajaj", "roll": "113", "github":"https://github.com/113suruchi", "linkedin":"linkedin.com/suruchi-bajaj/"}
    ],
    "ppc": [
        {"name": "Alok Khalkho", "roll": "009", "github":"https://github.com/Alok371", "linkedin":"https://www.linkedin.com/in/alok-khalkho-753978202"},
        {"name": "Bikky Sharma", "roll": "025", "github":"https://github.com/letscode-025", "linkedin":"https://www.linkedin.com/in/bikky-sharma-2b3089203"},
        {"name": "Dvarkesh Gupta", "roll": "030", "github":"https://github.com/Dvarkesh030", "linkedin":"https://www.linkedin.com/in/dvarkesh-gupta-357839203"},
        {"name": "Khushboo Khanchandani", "roll": "041", "github":"https://github.com/041khushboo", "linkedin":"https://www.linkedin.com/in/041-khushboo"},
        {"name": "Kunal Kumawat", "roll": "045", "github":"", "linkedin":""},
        {"name": "Mayank Kumar Singh", "roll": "051", "github":"https://github.com/Mayank0010", "linkedin":"https://www.linkedin.com/in/mayank-kumar-singh-45b500203"},
        {"name": "Neetu Meena", "roll": "060", "github":"https://github.com/neetumeena60", "linkedin":"https://www.linkedin.com/in/neetu meena"},
        {"name": "Nitesh Agrahari", "roll": "064", "github":"https://github.com/niteshagrahari", "linkedin":"https://www.linkedin.com/in/nitesh-agrahari-abb312203"},
        {"name": "Prateek Dubey", "roll": "075", "github":"https://github.com/075prateek", "linkedin":"https://www.linkedin.com/in/prateekdubey9584@gmail.com"},
        {"name": "Praveen Kumar Vishwakarma", "roll": "076", "github":"https://github.com/@praveen178", "linkedin":"https://www.linkedin.com/in/Praveen vishwakarma"},
        {"name": "Sheetal Ingle", "roll": "096", "github":"", "linkedin":""},
        {"name": "Shivam Singh", "roll": "098", "github":"https://github.com/neo24061998", "linkedin":"https://www.linkedin.com/in/shivam098"},
        {"name": "Shubham Brajwasi", "roll": "100", "github":"https://github.com/100shubham", "linkedin":"https://www.linkedin.com/in/shubham brajwasi"},
        {"name": "Shubham Sharma", "roll": "101", "github":"https://github.com/ 101shubham", "linkedin":"https://www.linkedin.com/in/101shubham"},
        {"name": "Shyam Shukla", "roll": "102", "github":"https://github.com/tecnofyle", "linkedin":"https://www.linkedin.com/in/tecnofyle"},
        {"name": "Vandana Mandloi", "roll": "107", "github":"https://github.com/vandanamandloi107", "linkedin":"https://www.linkedin.com/in/vandanamandloi"}
    ],
    "arc": [
        {"name": "Aman Shrivansh", "roll": "011", "github":"https://github.com/Aman0110-bot", "linkedin":"https://www.linkedin.com/in/Aman Shrivansh"},
        {"name": "Amar Sarkar", "roll": "012", "github":"https://github.com/amarua", "linkedin":"https://www.linkedin.com/in/amar-sarkar-211842203/"},
        {"name": "Asish Chowdhury", "roll": "023", "github":"https://github.com/023-Asish", "linkedin":"https://www.linkedin.com/in/asish-chowdhury-0bb3b6203"},
        {"name": "Jayshree Choudhary", "roll": "038", "github":"https://github.com/Jayshree-038", "linkedin":"https://www.linkedin.com/in/038jayshree"},
        {"name": "Kajal Nerkar", "roll": "039", "github":"https://github.com/39-KAJAL", "linkedin":"https://www.linkedin.com/in/Kajal Nerkar"},
        {"name": "KM Sarita Chaudhary", "roll": "044", "github":"https://github.com/sarita1997", "linkedin":"https://www.linkedin.com/in/SARITA CHAUDHARY"},
        {"name": "Moh Azhar Hussain", "roll": "052", "github":"https://github.com/azhar52", "linkedin":"https://www.linkedin.com/in/azhar-hussain-a62218203"},
        {"name": "Neetu Pandit", "roll": "061", "github":"https://github.com/NeetuPandit", "linkedin":"https://www.linkedin.com/in/NEETU PANDIT"},
        {"name": "Pooja Yadav", "roll": "072", "github":"https://github.com/072-Poojaydv", "linkedin":"https://www.linkedin.com/in/pooja-yadav-53b132203"},
        {"name": "Prashansa Geete", "roll": "073", "github":"", "linkedin":""},
        {"name": "Rajni Kasotiya", "roll": "080", "github":"https://github.com/rajnikasotiya", "linkedin":"https://www.linkedin.com/in/rajni-kasotiya-a02210203"},
        {"name": "Ruchi Panse", "roll": "083", "github":"https://github.com/ruchi083", "linkedin":"https://www.linkedin.com/in/panseruchi83"},
        {"name": "Sagar Gupta", "roll": "086", "github":"https://github.com/sagarg86", "linkedin":"https://www.linkedin.com/in/sagar-gupta86"},
        {"name": "Saloni Pawar", "roll": "087", "github":"https://github.com/saloni087", "linkedin":"https://www.linkedin.com/in/ saloni-pawar-82b3a8202"},
        {"name": "Sangam Raja", "roll": "089", "github":"https://github.com/089-sangam", "linkedin":"https://www.linkedin.com/in/sangam-raja-984774191"},
        {"name": "Sarath Kumar", "roll": "091", "github":"https://github.com/sksarathkumarsk", "linkedin":"https://www.linkedin.com/in/sarath-kumar-8089a017a"},
        {"name": "Sudhanshu", "roll": "105", "github":"https://github.com/Sudhanshu-105", "linkedin":"https://www.linkedin.com/in/sudhanshu-shrivastava-74a089203"}
    ],
    "prc": [
        {"name": "Aditya Kumar Soni", "roll": "004", "github":"https://github.com/04adityasoni", "linkedin":"https://www.linkedin.com/in/adityasoni1107"},
        {"name": "Akshay Gawai", "roll": "008", "github":"https://github.com/0008akshay", "linkedin":"https://www.linkedin.com/in/akshay-gawai-6b24b3203"},
        {"name": "Amit Kumar Maddhesiya", "roll": "016", "github":"https://github.com/amit5720", "linkedin":"https://www.linkedin.com/in/amit-kumar-maddheshiya-379a02202"},
        {"name": "Dipesh Mandloi", "roll": "029", "github":"https://github.com/DIPESH29", "linkedin":"https://www.linkedin.com/in/DIPESH029"},    
        {"name": "Khushbu Mourya", "roll": "042", "github":"https://github.com/Khushbu042", "linkedin":"https://www.linkedin.com/in/Khushbu mourya"},
        {"name": "Kishan Dwivedi", "roll": "043", "github":"https://github.com/043-kishan", "linkedin":"https://www.linkedin.com/in/kishan-dwivedi-72a199201"},
        {"name": "Manish Kumar", "roll": "048", "github":"https://github.com/manish123k", "linkedin":"https://www.linkedin.com/in/manish123k"},
        {"name": "Neeraj Upadhyay", "roll": "059", "github":"https://github.com/neeraj-059", "linkedin":"https://www.linkedin.com/in/neeraj-upadhyay-145202203"},
        {"name": "Nitansshu Jain ", "roll": "063", "github":"https://github.com/nitansshujain", "linkedin":"https://www.linkedin.com/in/nitansshujain"},
        {"name": "Nitesh Kumar", "roll": "065", "github":"https://github.com/Nitesh02900", "linkedin":"https://www.linkedin.com/in/NITESH KUMAR"},
        {"name": "Nitin Dayar", "roll": "066", "github":"https://github.com/nitindayar", "linkedin":"https://www.linkedin.com/in/nitin-dayar-/"},
        {"name": "Prashant Shukla", "roll": "074", "github":"https://github.com/74prashant", "linkedin":"https://www.linkedin.com/in/74prashant"},
        {"name": "Puneet Kumar", "roll": "078", "github":"https://github.com/78puneet", "linkedin":"https://www.linkedin.com/in/Puneet Kumar"},
        {"name": "Rishikant Patel", "roll": "082", "github":"https://github.com/082-Rishikant", "linkedin":"https://www.linkedin.com/in/082-Rishikant"},
        {"name": "Sanskar Dhanotiya", "roll": "090", "github":"https://github.com/90sanskardhanotiya", "linkedin":"https://www.linkedin.com/in/sanskar-dhanotiya-9961ba203"},
        {"name": "Shababul Ali", "roll": "093", "github":"https://github.com/shababul093", "linkedin":"https://www.linkedin.com/in/shababul-ali-093"},
        {"name": "Shashank Shekhar Pandey", "roll": "095", "github":"https://github.com/shashank095", "linkedin":"https://www.linkedin.com/in/shashank shekhar pandey"},
    ],
    "rc": [
        {"name": "Aditya Kumar Soni", "roll": "004", "github":"https://github.com/04adityasoni", "linkedin":"https://www.linkedin.com/in/adityasoni1107"},
        ],
}