# test_r7_07.py
# coding: utf-8
'''
解析为下边的Lua格式，reward_type固定为REWARD_TYPE_ITEM，并保存到reward.lua文件中

{
    [1] = {
      [1] = {reward_type = REWARD_TYPE_ITEM, item_type = 2001, item_count = 80,},
      [2] = {reward_type = REWARD_TYPE_ITEM, item_type = 2004, item_count = 80,},
      [3] = {reward_type = REWARD_TYPE_ITEM, item_type = 3001, item_count = 25,},
      [4] = {reward_type = REWARD_TYPE_ITEM, item_type = 6101, item_count = 11,},
    },
    [2] = {
      [1] = {reward_type = REWARD_TYPE_ITEM, item_type = 2001, item_count = 70,},
      [2] = {reward_type = REWARD_TYPE_ITEM, item_type = 2004, item_count = 70,},
      [3] = {reward_type = REWARD_TYPE_ITEM, item_type = 3002, item_count = 20,},
    },
    [3] = {
      [1] = {reward_type = REWARD_TYPE_ITEM, item_type = 2001, item_count = 60,},
      [2] = {reward_type = REWARD_TYPE_ITEM, item_type = 2004, item_count = 60,},
      [3] = {reward_type = REWARD_TYPE_ITEM, item_type = 3003, item_count = 15,},
      [4] = {reward_type = REWARD_TYPE_ITEM, item_type = 6103, item_count = 13,},
    },
}

'''