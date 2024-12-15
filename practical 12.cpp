/*  Write program to implement a priority queue in C++ using an 
inorder list to store the items in the queue. Create a class that includes the data items (which 
should be template) and the priority (which should be int). The inorder list should contain 
these objects, with operator <= overloaded so that the items with highest priority appear at 
the beginning of the list (which will make it relatively easy to retrieve the highest item.)   */

#include <iostream>
#include <list>
#include <iterator>
using namespace std;

template <typename T>
class PriorityItem {
public:
    T data;
    int priority;
    PriorityItem(T d, int p) : data(d), priority(p) {}
    bool operator<=(const PriorityItem<T>& other) const {
        return this->priority >= other.priority;
    }
};

template <typename T>
class PriorityQueue {
private:
    list<PriorityItem<T>> queue;

public:
    void enqueue(T data, int priority) {
        PriorityItem<T> newItem(data, priority);
        auto it = queue.begin();
        while (it != queue.end() && *it <= newItem) {
            ++it;
        }
        queue.insert(it, newItem);
    }

     T dequeue() {
        if (queue.empty()) {
            throw underflow_error("Queue is empty!");
        }
        T highestPriorityData = queue.front().data;
        queue.pop_front();
        return highestPriorityData;
    }

    bool isEmpty() const {
        return queue.empty();
    }

    void display() const {
        for (const auto& item : queue) {
            cout << "Data: " << item.data << ", Priority: " << item.priority << endl;
        }
    }
};

int main() {
    PriorityQueue<string> pq;

    pq.enqueue("Task1", 3);
    pq.enqueue("Task2", 5);
    pq.enqueue("Task3", 1);
    pq.enqueue("Task4", 4);

    cout << "Priority Queue after enqueuing tasks:" << endl;
    pq.display();

    cout << "\nDequeue highest-priority task: " << pq.dequeue() << endl;

    cout << "\nPriority Queue after dequeue:" << endl;
    pq.display();

    return 0;
}
