# Artificial-Intelligence-AI-
1. Giới thiệu về đồ án
   Đồ án này là một ứng dụng phần mềm được phát triển để trực quan hóa quá trình giải quyết bài toán 8 Quân Xe. Ứng dụng giúp người dùng, đặc biệt là sinh viên và người học về Trí tuệ Nhân tạo, hiểu rõ hơn cách các thuật toán tìm kiếm hoạt động trong một bài toán cụ thể. Giao diện trực quan cho phép người dùng theo dõi từng bước đi của thuật toán, qua đó phân tích được ưu và nhược điểm của từng phương pháp. Mục tiêu của đề tài là biến những lý thuyết khô khan thành những hình ảnh trực quan để dễ quan sát và tìm hiểu.
2. Phân tích bài toán
   Ở đề tài này, em đã xây dựng bài toán đặt 8 quân xe lên bàn cờ 8x8 sao cho hai quân xe không tấn công lẫn nhau, tức là 2 quân xe không được nằm trên cũng 1 hàng hay 1 cột. Bài toán này có thể hiểu như là bài toán tìm kiếm không gian trạng với:
       Trạng thái ban đầu: bàn cờ trống 8x8
       Trạng thái mục tiêu: các quân xe đã được đặt đúng hàng và cột, mỗi hàng và mỗi cột chỉ được đặt một quân xe.
       Toán tử: đặt một quân xe vào vị trí hợp lệ trên bàn cờ.

3. Các tính năng chính
   Giao diên người dùng (gui)
     Ứng dụng sẽ sử dụng ngôn ngữ lập trình Python kết hợp với sử dụng thu viện Tkinker để thiết kế giao diện đồ họa. Giao diện gồm các thành phần như:
       Bàn cờ 8x8: bàn cờ bên trái là bàn cờ trống (chưa đặt quân xe nào), bàn cờ bên phải là bàn cờ thể hiện trạng thái khi đặt các quân xe.
       Bảng điều khiển: sẽ có một danh sách các thuật toán để chọn như: BFS, DFS, DLS,....
       Các nút chức năng: cho phép người dùng "Bắt đầu", "Dừng", "Reset" và chọn "Phương án tiếp theo của thuật toán
       Thanh tùy chỉnh: cho phép điều khiển "Tốc độ" thực thi của bài toán ( ở thanh này em làm bị ngược, tốc độ càng chậm bài toán càng nhanh), và thanh "DLS-limit" để giới hạn độ sâu cho thuật toán DLS
   Module thuật toán ( search_algrithsm)
   ở module này nó sẽ chứa tất cả mã nguồn của các thuật toán tìm kiếm. Mỗi thuật toán sẽ được lập trình để nhận trạng thái của bài cờ, sau đố thực hiện các bước tìm kiếm để trả về trạng thái của bàn cờ tiếp theo cho GUI để hiện thị ra màn hình.
4. Phân tích các thuật toán
   Trò chơi sẽ giúp trực quan hóa cách mà từng thuật toán giải quyết bài toán đặt 8 quân xe với các nhóm thuật toán sau:
   Tìm kiếm không có thông tin
   BFS(Breadth-First Search): Thuật toán này tìm kiếm theo chiều rộng. Nó khám phá tất cả các nút ở cùng một mức trước khi chuyển sang mức sâu hơn. Nhược điểm của BFS là tốn bộ nhớ vì phải lưu trữ tất cả các nút đã thăm.
   DFS(Depth-First Search): Thuật toán này tìm kiếm theo chiều sâu. Nó đi sâu vào một nhánh cho đến khi tìm thấy lời giải hoặc hết đường, sau đó quay lại. Ưu điểm là tiết kiệm bộ nhớ, nhưng có thể mất nhiều thời gian nếu lời giải nằm ở nhánh khác và nó đi sâu vào một nhánh không có lời giải.
   IDS (Iterative Deepening Search) là một sự kết hợp thông minh giữa BFS và DFS, thực hiện tìm kiếm theo chiều sâu nhưng có giới hạn độ sâu tăng dần sau mỗi lần lặp. Điều này giúp IDS vừa hiệu quả về mặt bộ nhớ (như DFS) vừa đảm bảo tìm được lời giải ngắn nhất (như BFS).
   Tìm kiếm có thông tin
   Greedy: Thuật toán này là một loại tìm kiếm có thông tin. Nó sử dụng một hàm heuristic (h) để ước tính chi phí từ trạng thái hiện tại đến trạng thái mục tiêu và luôn chọn nút có chi phí ước tính thấp nhất để mở rộng. Ưu điểm của thuật toán là nó thường tìm thấy một lời giải rất nhanh, nhưng nhược điểm là không đảm bảo tìm thấy lời giải tối ưu hoặc lời giải tốt nhất.
   A*: là một trong những thuật toán tìm kiếm thông minh và hiệu quả nhất. Nó kết hợp cả chi phí thực tế đã đi (g) và chi phí ước tính đến mục tiêu (h) để tìm đường đi tối ưu. Ưu điểm của A* là tìm được đường đi tối ưu và hiệu quả hơn nhiều so với các thuật toán tìm kiếm mù, vì nó có "trí tuệ" để ước tính con đường tốt nhất. Tuy nhiên, nhược điểm là việc chọn một hàm heuristic ($h$) không chính xác có thể làm giảm hiệu quả của thuật toán.
   UCS(Uniform Cost Search): Thuật toán này là một biến thể của BFS, ưu tiên mở rộng các nút có chi phí đường đi từ gốc nhỏ nhất. Ưu điểm của UCS là nó đảm bảo tìm được lời giải tối ưu, đặc biệt khi các bước đi có chi phí không đồng đều. Nhược điểm của nó là có thể tốn rất nhiều thời gian và bộ nhớ, tương tự như BFS, đặc biệt trong những trường hợp mà chi phí các bước đi nhỏ và bằng nhau.
   Tìm kiếm cục bộ
   Hill Climbing (Leo đồi):  là một thuật toán tìm kiếm cục bộ đơn giản và tham lam. Nó bắt đầu từ một trạng thái ngẫu nhiên và liên tục di chuyển đến một trạng thái "tốt hơn" gần đó (trạng thái có giá trị heuristic cao hơn), giống như leo lên một ngọn đồi để tìm đỉnh. Ưu điểm của nó là cực kỳ đơn giản, dễ thực hiện và tiết kiệm bộ nhớ. Nhược điểm lớn nhất là nó có thể bị mắc kẹt tại một đỉnh cục bộ (local maximum) và không thể tìm thấy đỉnh cao nhất (global maximum) của không gian tìm kiếm.
   Simulated Annealing (Giải nhiệt mô phỏng):  là một thuật toán cải tiến từ Hill Climbing, lấy cảm hứng từ quá trình làm nguội kim loại. Thuật toán này không chỉ chấp nhận các bước di chuyển lên "đồi" (trạng thái tốt hơn) mà còn có một xác suất chấp nhận các bước đi xuống "thung lũng" (trạng thái tồi tệ hơn) để tránh bị kẹt tại đỉnh cục bộ. Xác suất này giảm dần theo thời gian, giống như việc nhiệt độ giảm dần. Ưu điểm là nó có khả năng thoát khỏi các cực đại cục bộ và tìm được lời giải gần tối ưu hơn. Nhược điểm là việc chọn các tham số (như tốc độ giảm nhiệt) có thể rất khó khăn và tốn thời gian.
   Genetic Algorithm (Thuật toán di truyền): là một thuật toán tìm kiếm dựa trên nguyên lý tiến hóa tự nhiên của Darwin. Thuật toán này làm việc với một tập hợp các lời giải tiềm năng (quần thể - population), sau đó sử dụng các phép toán như chọn lọc, lai ghép (crossover) và đột biến (mutation) để tạo ra một thế hệ lời giải mới tốt hơn. Ưu điểm của nó là rất mạnh mẽ trong việc giải các bài toán tối ưu hóa phức tạp và có không gian tìm kiếm rộng lớn. Nhược điểm là nó không đảm bảo tìm ra lời giải tối ưu tuyệt đối và việc mã hóa bài toán thành các "cá thể" (individuals) có thể phức tạp.
   Beam Search: Thuật toán này là một thuật toán tìm kiếm hiệu quả, kết hợp các yếu tố của BFS và Greedy Search. Nó mở rộng một số lượng nút giới hạn ở mỗi cấp độ của cây tìm kiếm, thay vì tất cả các nút như BFS. Cụ thể, nó chỉ giữ lại $k$ nút tốt nhất (tức là k "tia sáng" - beams) để mở rộng cho bước tiếp theo. Ưu điểm của Beam Search là hiệu quả về mặt thời gian và bộ nhớ hơn so với BFS, vì nó không cần khám phá toàn bộ không gian tìm kiếm. Tuy nhiên, nhược điểm là nó không đảm bảo tìm được lời giải tối ưu vì nó có thể bỏ qua các nút tiềm năng nếu chúng không nằm trong k$nút tốt nhất ở một cấp độ nào đó.
   Ngoài ra còn có các thuật toán khác như:
   AND-OR Graph Search: Thuật toán này được sử dụng để giải quyết các bài toán có cấu trúc phân rã, thường được biểu diễn dưới dạng cây tìm kiếm AND-OR. Nó khác với các thuật toán tìm kiếm truyền thống (như BFS hoặc DFS) vì mục tiêu không chỉ là tìm một đường đi duy nhất từ trạng thái ban đầu đến trạng thái mục tiêu, mà là tìm một "lời giải" được tạo thành từ nhiều con đường khác nhau.
   DLS: Thuật toán này là một biến thể của DFS (Tìm kiếm theo chiều sâu). Nó hoạt động tương tự như DFS, nhưng có một tham số bổ sung là giới hạn độ sâu ($L$). Thuật toán sẽ đi sâu vào một nhánh cho đến khi tìm thấy lời giải hoặc đạt đến giới hạn độ sâu đã định, sau đó quay lại.

4. Mô phỏng các thuật toán
   4.1 Tìm kiếm có thông tin 
   
