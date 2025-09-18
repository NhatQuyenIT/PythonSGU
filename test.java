import java.util.*;

class Product {
    private String id;
    private String name;
    private double price;

    public Product(String id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public String getId() { return id; }
    public String getName() { return name; }
    public double getPrice() { return price; }

    @Override
    public String toString() {
        return id + " - " + name + " - " + price + " VND";
    }
}

class CartItem {
    private Product product;
    private int quantity;

    public CartItem(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
    }

    public Product getProduct() { return product; }
    public int getQuantity() { return quantity; }
    public double getTotal() { return product.getPrice() * quantity; }
}

class Cart {
    private List<CartItem> items = new ArrayList<>();

    public void addItem(Product product, int quantity) {
        items.add(new CartItem(product, quantity));
    }

    public double getTotal() {
        double total = 0;
        for (CartItem item : items) {
            total += item.getTotal();
        }
        return total;
    }

    public void printReceipt() {
        System.out.println("===== HÓA ĐƠN =====");
        for (CartItem item : items) {
            System.out.printf("%s x%d: %.2f VND\n", item.getProduct().getName(), item.getQuantity(), item.getTotal());
        }
        System.out.println("-------------------");
        System.out.printf("Tổng cộng: %.2f VND\n", getTotal());
    }
}

public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Danh sách sản phẩm mẫu
        List<Product> products = Arrays.asList(
            new Product("P01", "Sữa tươi", 25000),
            new Product("P02", "Bánh mì", 12000),
            new Product("P03", "Nước ngọt", 15000)
        );

        Cart cart = new Cart();
        while (true) {
            System.out.println("Danh sách sản phẩm:");
            for (Product p : products) {
                System.out.println(p);
            }
            System.out.print("Nhập mã sản phẩm (hoặc 'exit' để tính tiền): ");
            String id = sc.nextLine();
            if (id.equalsIgnoreCase("exit")) break;

            Product selected = null;
            for (Product p : products) {
                if (p.getId().equalsIgnoreCase(id)) {
                    selected = p;
                    break;
                }
            }
            if (selected == null) {
                System.out.println("Không tìm thấy sản phẩm!");
                continue;
            }
            System.out.print("Nhập số lượng: ");
            int qty = Integer.parseInt(sc.nextLine());
            cart.addItem(selected, qty);
        }
        cart.printReceipt();
        sc.close();
    }
}