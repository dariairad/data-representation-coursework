# Lab 04 - Implement all the API calls (as functions)

import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"An Error Occured. Error Code {response.status_code}")


def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"An Error Occured. Error Code {response.status_code}")

def createBook(book):
    response = requests.post(url, json=book)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"An Error Occured. Error Code {response.status_code}")

def updateBook(id, diffbook):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=diffbook)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"An Error Occured. Error Code {response.status_code}")


def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"An Error Occured. Error Code {response.status_code}")

if __name__ == "__main__":
    book = {
        "Author":"placeholder author",
        "Title":"placeholder title",
        "Price": 666
    }

    diffbook = {
        "Price": 100
    }
    
    #print(getAllBooks())
    #print(getBookById(423))
    #print(createBook(book))
    #print(updateBook(424, diffbook))
    print(deleteBook(426))
 
