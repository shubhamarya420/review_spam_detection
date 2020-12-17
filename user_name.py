def username(arr):
    c=0
    a=["sennheiser","jbl","sony","boat","mi","samsung","realme","jockey","tata","raymonds","hp","dell","mavic","drone","woodland","redchief","pepsodent","modi","iit","cocacola","puma","flipkart","starbuks","kfc","cobra","gucci","channel","anglepriya","somanbefawaha","tomyhighflyer"]
    k=arr.lower()
    for i in a:
        if( i in k):
            return 1;
    return 0;


