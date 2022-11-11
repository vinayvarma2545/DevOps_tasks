db = db.getSiblingDB("test_db");
db.test_tb.drop();

db.test_tb.insertMany([
    {
        "testno": 1,
        "name": "frontend",
        "type": "offline"
    },
    {
        "testno": 2,
        "name": "backend",
        "type": "online"
    },
    {
        "testno": 3,
        "name": "devops",
        "type": "online"
    }
]);