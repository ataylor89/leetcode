mport java.util.Stack;

class MyQueue {

    private Stack<Integer> stack;
    private int front;
    
    /** Initialize your data structure here. */
    public MyQueue() {
        stack = new Stack<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        stack.push(x);
        
        if (stack.size() == 1)
            front = x;
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        Stack<Integer> save = new Stack<>();
        
        while (stack.size() > 1)
            save.push(stack.pop());
    
        int val = stack.pop();
        
        if (save.size() > 0) {
            this.front = save.pop();
            stack.push(this.front);
        }
        
        while (save.size() > 0) 
            stack.push(save.pop());
            
        return val;
    }
    
    /** Get the front element. */
    public int peek() {
        return front;
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack.isEmpty();
    }
}
