#include<iostream>
#include<vector>
#include<string>
using namespace std;

enum nodeType {BOOK, CHAPTER, SECTION, SUBSECT};

string getEnumString(nodeType type){
		string retval;
		switch(type){
			case BOOK: retval="Book"; break;
			case CHAPTER: retval="Chapter"; break;
			case SECTION: retval="\tSection"; break;
			case SUBSECT: retval="\t\tSubSection"; break;
			default: retval = "Undefined";
		}
		return retval;
	}

class node{
	int childCount;
	node * children[50];

public:
	nodeType type;
	string data;
	node():childCount(0){}
	node(nodeType tmptype,string tmpdata):type(tmptype),data(tmpdata),childCount(0){}
	~node(){
		for(int i = 0; i < childCount; i++){
			delete children[i];

		}
	}
	void addChild(nodeType tmptype,string tmpdata){
        children[childCount++] = new node(tmptype, tmpdata);
	}
	void display(){
		cout << getEnumString(type) << " : " << data << endl;
		for(int i = 0; i < childCount; i++){
			children[i]->display();
		}
	}
	node * find(string tmpdata){
	    for(int i = 0; i < childCount; i++){
			if(children[i]->data == tmpdata){
			    return children[i];
			}
		}
		return nullptr;
	}
};

class book{
	node root;
	public:
	book(string name){
	    root.type = BOOK;
	    root.data = name;
	}
	void addChapter(string ch){
		root.addChild(CHAPTER, ch);
	}
	void addSection(string ch, string sect){
		root.find(ch)->addChild(SECTION, sect);
	}
	void addSubSection(string ch, string sect,string ssect){
		root.find(ch)->find(sect)->addChild(SUBSECT, ssect);
	}
	void display(){
		root.display();
	}
};

int main(){
	book b("DSAL");
	b.addChapter("1");
	b.addSection("1", "1.1");
	b.addSubSection("1", "1.1", "1.1.1");
	b.addSubSection("1", "1.1", "1.1.2");
	b.addSection("1", "1.2");

   	b.display();
	return 0;
}
