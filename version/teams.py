import json

senior = {
    "ccc": [{"name": "Mayank Sharma", "roll": "010", "type": "Chairman", "github":"https://github.com/mayanknimcet188", "linkedin":"https://www.linkedin.com/in/mayank-sharma-57414b198/"}],
    "eec": [{"name": "Kuldeep Patidar", "roll": "011", "type": "Chairperson", "github":"https://github.com/kuldeeppatidar47kp", "linkedin":"https://www.linkedin.com/in/kuldeep-patidar-4870751b4"}],
    "prc": [{"name": "Surbhi Dabhade", "roll": "012", "type": "Chairperson", "github":"https://github.com/surbhidabhade", "linkedin":"https://www.linkedin.com/in/surbhi-dabhade-bb711319b/"}],
    "ppc": [{"name": "Anand Prakash", "roll": "013", "type": "Chairperson", "github":"https://github.com/a4anandprakash", "linkedin":"https://www.linkedin.com/in/a4anandprakash"}],
    "arc": [{"name": "Mahima Pandey", "roll": "014", "type": "Chairperson", "github":"https://github.com/mahii99p", "linkedin":"https://www.linkedin.com/in/mahima-pandey-a58abb1a1"}]
}

junior_head = {
    "ccc": [
        {"name": "Bhumika Khakha", "roll": "024", "type": "Secretary", "github":"https://github.com/bhumikakhakha", "linkedin":"http://linkedin.com/in/bhumikakhakha"},
        {"name": "Shivam Dubey", "roll": "097", "type": "Treasurer", "github":"https://github.com/stech0703", "linkedin":"https://www.linkedin.com/in/shivam-dubey-862086203/"}
    ],
    "eec": [
        {"name": "Nikita Das", "roll": "062", "type": "Web Team", "github":"https://github.com/nikki-99", "linkedin":"https://www.linkedin.com/in/nikita-das-517085203/"},
        {"name": "Amit Kumar", "roll": "015", "type": "Web Team", "github":"https://github.com/015amit", "linkedin":"https://www.linkedin.com/in/amit015/"},
        {"name": "Anshu Mala Lakra", "roll": "019", "type": "Web Team", "github":"https://github.com/019anshu", "linkedin":"https://www.linkedin.com/in/019anshu/"}
    ],
    "prc": 0,
    "ppc": 0,
    "arc": 0,
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
        {"name": "Aayushi", "roll": "002", "github":"", "linkedin":""},
        {"name": "Amitabha Roy", "roll": "013", "github":"", "linkedin":""},
        {"name": "Ankit Singh", "roll": "018", "github":"", "linkedin":""},
        {"name": "Charu Bajaj", "roll": "026", "github":"", "linkedin":""},
        {"name": "Deepeeka", "roll": "027", "github":"", "linkedin":""},
        {"name": "Dimple Gyanani", "roll": "028", "github":"", "linkedin":""},
        {"name": "Harshit Omar", "roll": "031", "github":"", "linkedin":""},
        {"name": "Harsh Rai", "roll": "032", "github":"", "linkedin":""},
        {"name": "Himanshi Bansal", "roll": "034", "github":"", "linkedin":""},
        {"name": "Hrishikant Mehta", "roll": "036", "github":"", "linkedin":""},
        {"name": "Jasbir Sikhawat", "roll": "037", "github":"", "linkedin":""},
        {"name": "Manish Kumar Pandey", "roll": "049", "github":"", "linkedin":""},
        {"name": "Manish Nangliya", "roll": "050", "github":"", "linkedin":""},
        {"name": "Pankaj Sharma", "roll": "068", "github":"", "linkedin":""},
        {"name": "Paras Tiwari", "roll": "069", "github":"", "linkedin":""},
        {"name": "Payal Soni", "roll": "070", "github":"", "linkedin":""},
        {"name": "Piyush Devda", "roll": "071", "github":"", "linkedin":""},
        {"name": "Sachin Lalwani", "roll": "084", "github":"", "linkedin":""},
        {"name": "Sachin Sharma", "roll": "085", "github":"", "linkedin":""},
        {"name": "Saurabh Anand", "roll": "092", "github":"", "linkedin":""},
        {"name": "Shanoor Ahmed", "roll": "094", "github":"", "linkedin":""},
        {"name": "Shobit Samaria", "roll": "099", "github":"", "linkedin":""},
        {"name": "Simran Garg", "roll": "103", "github":"", "linkedin":""},
        {"name": "Sonu Gupta", "roll": "104", "github":"", "linkedin":""},
        {"name": "Yasser Osman Khan", "roll": "110", "github":"", "linkedin":""},
        {"name": "Suruchi Bajaj", "roll": "113", "github":"", "linkedin":""}
    ],
    "ppc": [
        {"name": "Alok Khalkho", "roll": "009", "github":"", "linkedin":""},
        {"name": "Bikky Sharma", "roll": "025", "github":"", "linkedin":""},
        {"name": "Dvarkesh Gupta", "roll": "030", "github":"", "linkedin":""},
        {"name": "Khushboo Khanchandani", "roll": "041", "github":"", "linkedin":""},
        {"name": "Kunal Kumawat", "roll": "045", "github":"", "linkedin":""},
        {"name": "Mayank Kumar Singh", "roll": "051", "github":"", "linkedin":""},
        {"name": "Neetu Meena", "roll": "060", "github":"", "linkedin":""},
        {"name": "Nitesh Agrahari", "roll": "064", "github":"", "linkedin":""},
        {"name": "Prateek Dubey", "roll": "075", "github":"", "linkedin":""},
        {"name": "Praveen Kumar Vishwakarma", "roll": "076", "github":"", "linkedin":""},
        {"name": "Sheetal Ingle", "roll": "096", "github":"", "linkedin":""},
        {"name": "Shivam Singh", "roll": "098", "github":"", "linkedin":""},
        {"name": "Shubham Brajwasi", "roll": "100", "github":"", "linkedin":""},
        {"name": "Shubham Sharma", "roll": "101", "github":"", "linkedin":""},
        {"name": "Shyam Shukla", "roll": "102", "github":"", "linkedin":""},
        {"name": "Vandana Mandloi", "roll": "107", "github":"", "linkedin":""}
    ],
    "arc": [
        {"name": "Aman Shrivansh", "roll": "011", "github":"", "linkedin":""},
        {"name": "Amar Sarkar", "roll": "012", "github":"", "linkedin":""},
        {"name": "Asish Chowdhury", "roll": "023", "github":"", "linkedin":""},
        {"name": "Jayshree Choudhary", "roll": "038", "github":"", "linkedin":""},
        {"name": "Kajal Nerkar", "roll": "039", "github":"", "linkedin":""},
        {"name": "KM Sarita Chaudhary", "roll": "044", "github":"", "linkedin":""},
        {"name": "Moh Azhar Hussain", "roll": "052", "github":"", "linkedin":""},
        {"name": "Neetu Pandit", "roll": "061", "github":"", "linkedin":""},
        {"name": "Pooja Yadav", "roll": "072", "github":"", "linkedin":""},
        {"name": "Prashansa Geete", "roll": "073", "github":"", "linkedin":""},
        {"name": "Rajni Kasotiya", "roll": "080", "github":"", "linkedin":""},
        {"name": "Ruchi Panse", "roll": "083", "github":"", "linkedin":""},
        {"name": "Sagar Gupta", "roll": "086", "github":"", "linkedin":""},
        {"name": "Saloni Pawar", "roll": "087", "github":"", "linkedin":""},
        {"name": "Sangam Raja", "roll": "089", "github":"", "linkedin":""},
        {"name": "Sarath Kumar", "roll": "091", "github":"", "linkedin":""},
        {"name": "Sudhanshu", "roll": "105", "github":"", "linkedin":""}
    ],
    "prc": [
        {"name": "Aditya Kumar Soni", "roll": "004", "github":"", "linkedin":""},
        {"name": "Khushbu Mourya", "roll": "042", "github":"", "linkedin":""},
        {"name": "Kishan Dwivedi", "roll": "043", "github":"", "linkedin":""},
        {"name": "Manish Kumar", "roll": "048", "github":"", "linkedin":""},
        {"name": "Neeraj Upadhyay", "roll": "059", "github":"", "linkedin":""},
        {"name": "Nitansshu Jain ", "roll": "063", "github":"", "linkedin":""},
        {"name": "Nitesh Kumar", "roll": "065", "github":"", "linkedin":""},
        {"name": "Prashant Shukla", "roll": "074", "github":"", "linkedin":""},
        {"name": "Puneet Kumar", "roll": "078", "github":"", "linkedin":""},
        {"name": "Rishikant Patel", "roll": "082", "github":"", "linkedin":""},
        {"name": "Shababul Ali", "roll": "093", "github":"", "linkedin":""},
        {"name": "Shashank Shekhar Pandey", "roll": "095", "github":"", "linkedin":""}
    ],
}
