# Super Mario Party Jamboree (0100965017338000): the rewriter's patches of this game's own builds (dm/tools/patch_nso.py, "Registered patches")
CUTS = {
  # 1.0.0 (v0) main: nninitStartup (main+0x98281c) initializes malloc's StandardAllocator over 2 GB of address space (main+0x982834), then a second StandardAllocator with virtual
  # address memory over 56 GB (main+0x982840), which the Switch's 64 GB alias region holds and the host's 4.38 GB one cannot: CentralHeap::Init fails and Initialize aborts
  # (sdk+0x12b19c). With the sdk's node area and alignment cuts (dm/tools/sdk_patches.py) the alias region holds about 4.3 GB of regions: malloc 1 GB and the game's allocator 3 GB.
  # 2 + 2 GB ran the game's allocator dry at the opening movie (CoreSystem::Allocate null, main+0x8516dc); 2 + 0.5 GB at the first NVN memory pools. Both commit pages as they go and
  # the pool (3.2 GB) bounds what they map. Measured on the Mac: 60 s at 60 fps through the opening movie
  'd70ce1726c979e45ed4200e9c2b23b2a': [
    (0x982838, '0100b052', '0100a852', 'malloc\'s StandardAllocator: address space mov w1,#0x80000000 → mov w1,#0x40000000 (2 GB → 1 GB)'),
    (0x982840, 'c801c0d2', '0800b8d2', 'StandardAllocator::Initialize(nullptr, size): address space mov x8,#0xe00000000 → mov x8,#0xc0000000 (56 GB → 3 GB)'),
  ],
}
