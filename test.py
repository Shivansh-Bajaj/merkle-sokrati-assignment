from __future__ import absolute_import
from horizontal_distance import *;
import pytest;


@pytest.fixture()
def complete_tree():
  return Tree().build([1,2,3,4,5,6,7])
@pytest.fixture()
def incomplete_tree():
  return Tree().build([1,2,3,4,-1,6,7,8,9,-1,-1,10,-1,11])
@pytest.fixture()
def duplicates_on_different_level_tree():
  return Tree().build([1,2,3,4,-1,6,7,8,7,-1,-1,10,-1,11])
@pytest.fixture()
def duplicates_on_same_level_tree():
  return Tree().build([1,2,3,4,-1,6,7,8,9,-1,-1,5,-1,8])



class TestHorizonalDistance(object):
  def test_complete_tree(self, complete_tree):
    assert HorizontalDistance().find(complete_tree, 1, 7) == -1, "key1 and key2 not on same level should give -1"
    assert HorizontalDistance().find(complete_tree, 4, 7) == 3, "happy case"
    assert HorizontalDistance().find(complete_tree, 5, 7) == 2, "happy case"
    assert HorizontalDistance().find(complete_tree, 7, 7) == 0, "key1 == key2 should return 0"
    assert HorizontalDistance().find(complete_tree, 7, None) == -1, "key1, key2 and root node should not be none"

  def test_incomplete_tree(self, incomplete_tree):
    assert HorizontalDistance().find(incomplete_tree, 8, 11) == 6, "it should consider empty nodes"
    assert HorizontalDistance().find(incomplete_tree, 8, 11) == 6, "it should consider empty nodes"

  def test_duplicates_on_different_level_tree(self, duplicates_on_different_level_tree):
    assert HorizontalDistance().find(duplicates_on_different_level_tree, 7, 11) == 5, "it should search on second level in case of duplicates"
    assert HorizontalDistance().find(duplicates_on_different_level_tree, 7, 4) == 3, "it should search on first level in case of duplicates"

  def test_duplicates_on_same_level_tree(self, duplicates_on_same_level_tree):
    assert HorizontalDistance().find(duplicates_on_same_level_tree, 5, 8) == 4, "it should count with first node in case of duplicates on same level"
