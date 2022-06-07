#!/usr/bin/env python3

from my_solution import createTree

# 测试用例
def test_solution():
    dataset = [['<=30', 'high', 'no', 'fair', 'no'],
               ['<=30', 'high', 'no', 'excellent', 'no'],
               ['31...40', 'high', 'no', 'fair', 'yes'],
               ['>40', 'medium', 'no', 'fair', 'yes'],
               ['>40', 'low', 'yes', 'fair', 'yes'],
               ['>40', 'low', 'yes', 'excellent', 'no'],
               ['31...40', 'low', 'yes', 'excellent', 'yes'],
               ['<=30', 'medium', 'no', 'fair', 'no'],
               ['<=30', 'low', 'yes', 'fair', 'yes'],
               ['>40', 'medium', 'yes', 'fair', 'yes'],
               ['<=30', 'medium', 'yes', 'excellent', 'yes'],
               ['31...40', 'medium', 'no', 'excellent', 'yes'],
               ['31...40', 'high', 'yes', 'fair', 'yes'],
               ['>40', 'medium', 'no', 'excellent', 'no']]
    labels = [
        'age', 'income', 'student', 'credit_rating', 'Class:buy_computer'
    ]
    # 正确答案
    correct_solution = {'age':
                            {'<=30':
                                 {'student':
                                      {'no': 'no', 'yes': 'yes'}},
                             '>40':
                                 {'credit_rating':
                                      {'excellent': 'no', 'fair': 'yes'}},
                             '31...40':
                                 'yes'}
                        }
    # 程序求解结果
    result=createTree(dataset, labels)
    assert correct_solution == result