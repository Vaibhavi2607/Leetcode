class RandomizedSet {
    ArrayList<Integer> list;

    public RandomizedSet() {
        list = new ArrayList<>();
    }

    public boolean insert(int val) {
        if (list.contains(val))
            return false;

        list.add(val);
        return true;
    }

    public boolean remove(int val) {
        if (list.contains(val)) {
            list.remove((Integer) val);
            return true;
        }

        return false;
    }

    public int getRandom() {
        Random rand = new Random();
        int index = rand.nextInt(0, list.size());
        return list.get(index);
    }
}