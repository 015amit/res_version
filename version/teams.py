import json

senior = {
    "ccc": [{"name": "Mayank Sharma", "roll": "010"}],
    "eec": [{"name": "Kuldeep Patidar", "roll": "011"}],
    "prc": [{"name": "Surbhi Dabhade", "roll": "012"}],
    "ppc": [{"name": "Anand Prakash", "roll": "013"}],
    "arc": [{"name": "Mahima Pandey", "roll": "014"}]
}

junior_head = {
    "ccc": [
        {"name": "Bhumika Khakha", "roll": "024", "type": "Secretary"},
        {"name": "Shivam Dubey", "roll": "097", "type": "Treasurer"}
    ],
    "eec": [
        {"name": "Nikita Das", "roll": "062", "type": "Web Team"},
        {"name": "Amit Kumar", "roll": "015", "type": "Web Team"},
        {"name": "Anshu Mala Lakra", "roll": "019", "type": "Web Team"}
    ],
    "prc": 0,
    "ppc": 0,
    "arc": 0,
}

data = {
    "ccc": [
        
            {"name": "Akriti Upadhyay", "roll": "007"},
            {"name": "Amandeep Yadav", "roll": "010"},
            {"name": "Himanshu Ghorwal", "roll": "035"},
            {"name": "Mahima Pawar", "roll": "047"},
            {"name": "Naman Tripathi", "roll": "054"},
            {"name": "Shivangi Gupta", "roll": "112"}
        
    ],
    "eec": [
        {"name": "Aayushi", "roll": "002"},
        {"name": "Amitabha Roy", "roll": "013"},
        {"name": "Ankit Singh", "roll": "018"},
        {"name": "Charu Bajaj", "roll": "026"},
        {"name": "Deepeeka", "roll": "027"},
        {"name": "Dimple Gyanani", "roll": "028"},
        {"name": "Harshit Omar", "roll": "031"},
        {"name": "Harsh Rai", "roll": "032"},
        {"name": "Himanshi Bansal", "roll": "034"},
        {"name": "Hrishikant Mehta", "roll": "036"},
        {"name": "Jasbir Sikhawat", "roll": "037"},
        {"name": "Manish Kumar Pandey", "roll": "049"},
        {"name": "Manish Nangliya", "roll": "050"},
        {"name": "Pankaj Sharma", "roll": "068"},
        {"name": "Paras Tiwari", "roll": "069"},
        {"name": "Payal Soni", "roll": "070"},
        {"name": "Piyush Devda", "roll": "071"},
        {"name": "Sachin Lalwani", "roll": "084"},
        {"name": "Sachin Sharma", "roll": "085"},
        {"name": "Saurabh Anand", "roll": "092"},
        {"name": "Shanoor Ahmed", "roll": "094"},
        {"name": "Shobit Samariya", "roll": "099"},
        {"name": "Simran Garg", "roll": "103"},
        {"name": "Sonu Gupta", "roll": "104"},
        {"name": "Yasser Osam Khan", "roll": "110"},
        {"name": "Suruchi Bajaj", "roll": "113"}
    ],
    "ppc": [
        {"name": "Alok Khalkho", "roll": "009"},
        {"name": "Bikky Sharma", "roll": "025"},
        {"name": "Dwarkesh Gupta", "roll": "030"},
        {"name": "Khushboo Khanchandani", "roll": "041"},
        {"name": "Kunal Kumawat", "roll": "045"},
        {"name": "Mayank Kumar Singh", "roll": "051"},
        {"name": "Neetu Meena", "roll": "060"},
        {"name": "Nitesh Agrahari", "roll": "064"},
        {"name": "Prateek Dubey", "roll": "075"},
        {"name": "Praveen Kumar Vishwakarma", "roll": "076"},
        {"name": "Sheetal Ingle", "roll": "096"},
        {"name": "Shivam Singh", "roll": "098"},
        {"name": "Shubham Brajwasi", "roll": "100"},
        {"name": "Shubham Sharma", "roll": "101"},
        {"name": "Shyam Shukla", "roll": "102"},
        {"name": "Vandana Mandloi", "roll": "107"}
    ],
    "arc": [
        {"name": "Aman Shrivansh", "roll": "011"},
        {"name": "Amar Sarkar", "roll": "012"},
        {"name": "Asish Chowdhury", "roll": "023"},
        {"name": "Jayshree Choudhary", "roll": "038"},
        {"name": "Kajal Nerkar", "roll": "039"},
        {"name": "KM Sarita Chaudhary", "roll": "044"},
        {"name": "Moh Azhar Hussain", "roll": "052"},
        {"name": "Neetu Pandit", "roll": "061"},
        {"name": "Pooja Yadav", "roll": "072"},
        {"name": "Prashansha Geete", "roll": "073"},
        {"name": "Rajni", "roll": "080"},
        {"name": "Ruchi Panse", "roll": "083"},
        {"name": "Sagar Gupta", "roll": "086"},
        {"name": "Saloni Pawar", "roll": "087"},
        {"name": "Sangam Raja", "roll": "089"},
        {"name": "Sarath Kumar", "roll": "091"},
        {"name": "Sudhanshu", "roll": "105"}
    ],
    "prc": [
        {"name": "Aditya Kumar Soni", "roll": "004"},
        {"name": "Khushbu Mourya", "roll": "042"},
        {"name": "Kishan Dwivedi", "roll": "043"},
        {"name": "Manish Kumar", "roll": "048"},
        {"name": "Neeraj Upadhyay", "roll": "059"},
        {"name": "Nitansshu Jain ", "roll": "063"},
        {"name": "Nitesh Kumar", "roll": "065"},
        {"name": "Prashant Shukla", "roll": "074"},
        {"name": "Puneet ", "roll": "078"},
        {"name": "Rishikant Patel", "roll": "082"},
        {"name": "Shababul Ali", "roll": "093"},
        {"name": "Shashank Shekhar Pandey", "roll": "095"}
    ],
}
