import numpy as np
import scipy.sparse as sp

# feature = sp.load_npz('data/DBLP/features_0.npz').toarray()
# print(feature.shape)
#
# a = np.load('data/DBLP/metapath2vec_emb_node.npy')
# b = np.load('data/DBLP/metapath2vec_emb_word.npy')
# print(a.shape)
# print(b.shape)
# adj1 = sp.load_npz('data/DBLP/adjM.npz').toarray()
# adj2 = sp.load_npz('data/DBLP/fuwuqi/adjM.npz').toarray()
# print(adj1.shape, adj2.shape)
# print(np.sum(adj1 - adj2))
# print(adj1[3])
# print(adj2[3])

# t1 = np.load('data/DBLP/fuwuqi/node_types.npy')
# t2 = np.load('data/DBLP/node_types.npy')
# print(t1.shape, t2.shape)
# print(np.sum(t1-t2))
# print(t1)
# print(t2)

train_val_test_idx = np.load('data/DBLP/train_val_test_idx.npz')
train_idx = train_val_test_idx['train_idx']
val_idx = train_val_test_idx['val_idx']
test_idx = train_val_test_idx['test_idx']
print(train_idx, val_idx, test_idx)

print('---------------------------------')
train_val_test_idx = np.load('data/DBLP/fuwuqi/train_val_test_idx.npz')
train_idx = train_val_test_idx['train_idx']
val_idx = train_val_test_idx['val_idx']
test_idx = train_val_test_idx['test_idx']
print(train_idx, val_idx, test_idx)