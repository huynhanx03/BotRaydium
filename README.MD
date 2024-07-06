# Raydium Telegram Bot

## Giới thiệu
Trong khuôn khổ của hoạt động Buidl Station diễn ra hàng tuần tại TPHCM, chúng tôi đã mở một bounty dành riêng cho những builders tham gia vào sự kiện.

## Chủ đề
Xây dựng telegram bot tương tác với Raydium

## Mô tả
Raydium là một trong những DEX lâu đời và nổi tiếng nhất trên mạng Solana. Bounty này yêu cầu người tham gia sẽ xây dựng một telegram bot hỗ trợ 3 câu lệnh sau:

- `/all-pools`: hiển thị tất cả các liquidity pools đang có trên Radium. (Tương tự như các pools hiển thị ở trang này https://raydium.io/liquidity-pools/?tab=all)

- `/concentrated-pools`: hiển thị tất cả các concentrated liquidity pools đang có trên Radium. (Tương tự như các pools hiển thị ở trang https://raydium.io/liquidity-pools/?tab=concentrated)

- `/standard-pools`: hiển thị tất cả các standard liquidity pools đang có trên Radium. (Tương tự như các pools hiển thị ở trang https://raydium.io/liquidity-pools/?tab=standard)

Mỗi pool sẽ bao gồm một số thông tin cơ bản như sau: token pair, liquidity, 24h volume, 24h fee and 24h APR.

## Hướng dẫn cài đặt
1. **Cài đặt python:**
   - Cài đặt phiên bản python phù hợp (đề nghị 3.10).

2. **Tải mã nguồn hoặc cài đặt Git:**
   - Nếu bạn đã cài đặt Git, thực hiện lệnh sau để sao chép mã nguồn:
     ```bash
     git clone https://github.com/huynhanx03/BotRaydium.git
     ```
   - Nếu bạn không có Git, bạn có thể tải mã nguồn từ [đây](https://github.com/hiephtdev/auto-trade-backpack/archive/refs/heads/master.zip) và giải nén nó.

3. **Cài đặt các gói phụ thuộc:**
   - Mở terminal hoặc command prompt và di chuyển đến thư mục dự án vừa sao chép.
   - Chạy lệnh sau để cài đặt các gói phụ thuộc:
     ```bash
     pip install python-telegram-bot requests
     ```

4. **Cài đặt bot**
   - Tìm liên hệ @BotFather ở telegram gõ /newbot để tạo bot mới để nhận token. 
   - Tạo file config.py tạo biến BOT_TOKEN với giá trị là token bot nhận được ở trên.

5. **Chạy ứng dụng:**
   - Sau khi cài đặt các gói phụ thuộc và điều chỉnh thông tin, bạn có thể khởi động ứng dụng bằng lệnh sau:
     ```bash
     py main.py
     ```