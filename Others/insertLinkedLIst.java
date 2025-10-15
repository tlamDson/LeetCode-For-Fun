package Others;

class DNode {

    int val;
    DNode next;
    DNode prev;

    DNode(int val) {
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {

    DNode head;
    DNode tail;  // Track tail for efficiency
    int size;

    DoublyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }

    // Insert val at index (0 = head, -1 = end)
    void insert(int index, int val) {

    }

    // Get val at index
    int get(int index) {
        if (index < 0 || index >= size || head == null) {
            throw new IndexOutOfBoundsException();
        } else {
            // Traverse to node before insertion point
            DNode c1 = head;
            int count = 0;
            while (count < index) {
                c1 = c1.next;
                count++;
            }
            return c1.val;
        }

    }

    // Add val to end
    void add(int val) {
        DNode newNode = new DNode(val);
        if (size == 0) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.prev = tail;
            tail.next = newNode;
            tail = newNode;
        }
        size++;

    }

    // Pop at index (default -1), return val
    int pop(int index) {
        if (size == 0) {
            return -1;
        } else {
            DNode c1 = head;
            int count = 0;
            while (count < index) {
                c1 = c1.next;
                count++;
            }
            DNode toremove = c1.next;
            c1.next = toremove.next;
            toremove.next.prev = c1;
            toremove.prev = null;
            toremove.next = null;

          

        }
        size--;
        return -1;
    }

    // Set val at index
    boolean set(int index, int val) {
        // Your code here
        return false;
    }

    // Helper: Print forward
    void print() {
        if (head == null) {
            System.out.println("Empty");
            return;
        }
        DNode curr = head;
        System.out.print(curr.val);
        curr = curr.next;
        while (curr != null) {
            System.out.print(" -> " + curr.val);
            curr = curr.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Same test as SLL
        DoublyLinkedList dll = new DoublyLinkedList();
        dll.add(1);
        dll.add(2);
        dll.insert(1, 10);
        dll.print();  // Expected: 1 -> 10 -> 2
    }
}
