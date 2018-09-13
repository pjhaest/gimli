#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import numpy as np
import pygimli as pg


class TestRVectorMethods(unittest.TestCase):

    def test_RVector(self):
        """ implemented in custom_rvalue.cpp"""
        a = pg.RVector(10)
        self.assertEqual(a.size(), 10.0)
        self.assertEqual(sum(a), 0.0)

    def test_ListToRVector3(self):
        """ implemented in custom_rvalue.cpp"""
        x = [0.0, 1.0, 0.0]
        p = pg.RVector3(x)
        self.assertEqual(p.dist(x), 0.0)
        self.assertEqual(p.dist([1.0, 1.0]), 1.0)

        p = pg.RVector3((0.0, 1.0, 0.0))
        self.assertEqual(p.dist([0.0, 1.0, 0.0]), 0.0)

    def test_ListToIndexArray(self):
        """ implemented in custom_rvalue.cpp"""
        idx = [0, 1, 1, 0]

        I = pg.IndexArray(idx)
        self.assertEqual(pg.sum(I), sum(idx))

        bn = (np.array(idx) > 0)  # numpy bool
        idx = np.nonzero(bn)[0]  # numpy int64

        # numyp int64 -> IndexArray
        I = pg.IndexArray(idx)

        self.assertEqual(I.size(), 2)
        self.assertEqual(pg.sum(I), sum(idx))

    def test_ListToRVector(self):
        """ implemented in custom_rvalue.cpp"""
        l = [1.0, 2.0, 3.0, 4.0]
        a = pg.RVector(l)
        self.assertEqual(a.size(), len(l))
        self.assertEqual(pg.sum(a), sum(l))

        l = (0.2, 0.3, 0.4, 0.5, 0.6)
        x = pg.RVector(l)
        self.assertEqual(x.size(), len(l))

        l = [1, 2, 3]
        x = pg.RVector(l)
        self.assertEqual(x.size(), len(l))

    def test_ListToR3Vector(self):
        """ implemented in custom_rvalue.cpp"""
        x = [0.0, 1.0, 0.0]
        p = pg.RVector3(x)
        pl = [p, p, p]
        t = pg.R3Vector(pl)
        self.assertEqual(t.size(), len(pl))

    def test_NumpyToIndexArray(self):
        """Implemented in custom_rvalue.cpp."""
        x = np.array(range(10))
        a = pg.IndexArray(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))

        x = np.arange(0, 10, dtype=np.int64)
        a = pg.IndexArray(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))

        x = np.arange(0, 10, dtype="int")
        a = pg.IndexArray(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))

        x = np.array([0, 100], dtype="int")
        a = pg.IndexArray(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))

    def test_NumpyToIVector(self):
        """Implemented in custom_rvalue.cpp."""
        x = np.array(range(-10, 10))
        a = pg.IVector(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))

        x = np.arange(-10, 10, dtype=np.int64)
        a = pg.IVector(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))

        x = np.arange(-10, 10, dtype="int")
        a = pg.IVector(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))

        x = np.array([-10, 100], dtype="int")
        a = pg.IVector(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))


    def test_NumpyToRVector(self):
        """Implemented in custom_rvalue.cpp."""
        x = np.arange(0, 1., 0.2)
        a = pg.RVector(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))

        x = np.arange(0, 1., 0.2, dtype=np.float64)
        a = pg.RVector(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))

        x = np.arange(10, dtype=np.int)
        a = pg.RVector(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))

        x = np.arange(10, dtype=np.long)
        a = pg.RVector(x)
        
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))
        
        self.assertEqual(pg.sum(x), sum(x))

    def test_NumpyToIVector(self):
        x = np.arange(10, dtype=np.long)
        a = pg.IVector(x)
        self.assertEqual(a.size(), len(x))
        self.assertEqual(pg.sum(a), sum(x))
        
        self.assertEqual(pg.sum(x), sum(x))
         
    def test_NumpyToCVector(self):
        pass
        # will not work .. until an idea how to choose right api for function with and RVector and CVector, e.g. sum()
        #
        #x = 1. + np.arange(0, 1., 0.1) * 1j
        #a = pg.CVector(x)

        #self.assertEqual(a.size(), len(x))
        #self.assertEqual(pg.real(a), x.real)
        #self.assertEqual(pg.imag(a), x.imag)
        #self.assertEqual(pg.sum(a), sum(x))

        #self.assertEqual(pg.sum(pg.real(a)), len(x))

    def test_NumpyToRMatrix(self):
        """Implemented in custom_rvalue.cpp."""
        M = np.ndarray((5, 4))
        A = pg.RMatrix(M)
        self.assertEqual(A.rows(), M.shape[0])
        self.assertEqual(A.cols(), M.shape[1])

        M = np.arange(20.).reshape((5, 4))
        A = pg.RMatrix(M)
        self.assertEqual(sum(A[0]), sum(M[0]))
        self.assertEqual(sum(A[1]), sum(M[1]))
        self.assertEqual(sum(A[2]), sum(M[2]))
        self.assertEqual(sum(A[3]), sum(M[3]))

    def test_NumpyToRVector3(self):
        """Implemented in custom_rvalue.cpp."""
        x = np.array([0.0, 1.0, 0.0])
        p = pg.RVector3(x)
        self.assertEqual(p.dist(x), 0.0)
        self.assertEqual(p.dist([1.0, 1.0]), 1.0)

        x = np.array([0.0, 1.0])
        p = pg.RVector3(x)
        self.assertEqual(p.dist([0.0, 1.0, 0.0]), 0.0)

    def test_RVectorToNumpy(self):
        """Implemented through hand_made_wrapper.py"""
        # check ob wirklich from array genommen wird!
        v = pg.RVector(10, 1.1)

        a = np.asarray(v)
        self.assertEqual(type(a), np.ndarray)
        self.assertEqual(len(a), 10)
        self.assertEqual(a[0], 1.1)

        a = np.asarray(v, "int")
        self.assertEqual(a[0], 1)

        a = np.array(v)
        self.assertEqual(type(a), np.ndarray)
        self.assertEqual(len(a), 10)

    def test_BVectorToNumpy(self):
        """Implemented through hand_made_wrapper.py"""
        # check ob wirklich from array genommen wird!
        # wird es noch nicht .. siehe __init__.py:__BVectorArrayCall__
        v = pg.RVector(10, 1)
        b = (v == 1)
        self.assertEqual(type(b), pg.BVector)
        
        v = pg.RVector(10, 1.1)
        b = (v == 1.1)
        self.assertEqual(type(b), pg.BVector)

        a = np.asarray(b)
        self.assertEqual(type(a), np.ndarray)
        self.assertEqual(a.dtype, 'bool')
        self.assertEqual(len(a), 10)
        self.assertEqual(sum(a), 10)

        a = np.array(b)
        self.assertEqual(type(a), np.ndarray)
        self.assertEqual(len(a), 10)
        self.assertEqual(sum(a), 10)

    def test_IndexArrayToNumpy(self):
        """Implemented through hand_made_wrapper.py"""
        # check if array is really taken
        # not yet taken: .. see __init__.py:__BVectorArrayCall__
        v = pg.IndexArray(10, 2)
        self.assertEqual(type(v), pg.IndexArray)
        # print(type(v[0]))
        # print(pg.showSizes())
        a = np.asarray(v)
        self.assertEqual(type(a), np.ndarray)
        # self.assertEqual(a.dtype, 'int64')
        self.assertEqual(len(a), 10)
        self.assertEqual(sum(a), 20)

        a = np.array(v)
        self.assertEqual(type(a), np.ndarray)
        self.assertEqual(len(a), 10)
        self.assertEqual(sum(a), 20)

    def test_RVector3ToNumpy(self):
        """Implemented through hand_made_wrapper.py"""
        v = pg.RVector3()

        a = np.array(v)
        self.assertEqual(type(a), np.ndarray)
        self.assertEqual(len(a), 3)

    def test_R3VectorToNumpy(self):
        """Implemented through hand_made_wrapper.py"""
        mesh = pg.createGrid(x=[0, 1, 2], y=[0, 1, 2], z=[1, 2])

        v = np.asarray(mesh.nodeCenters())

        self.assertEqual(type(v), np.ndarray)
        self.assertEqual(len(v), mesh.nodeCount())

        a = np.array(mesh.cellCenter())
        self.assertEqual(type(a), np.ndarray)
        self.assertEqual(len(a), mesh.cellCount())

        self.assertEqual(mesh.nodeCenters()[0], v[0])

    def test_RMatrixToNumpy(self):
        """Implemented through automatic iterator """
        M = np.arange(20.).reshape((5, 4))
        A = pg.RMatrix(M)
        N = np.array(A)
        self.assertEqual(A.rows(), N.shape[0])
        self.assertEqual(A.cols(), N.shape[1])
        self.assertEqual(sum(A[0]), sum(N[0]))
        self.assertEqual(sum(A[1]), sum(N[1]))
        self.assertEqual(sum(A[2]), sum(N[2]))
        self.assertEqual(sum(A[3]), sum(N[3]))

        M = np.arange(16.).reshape((4,4))
        A = pg.RMatrix(M)
        M2 = np.array(A)
        np.testing.assert_equal(M, M2)
        A = np.array(pg.RMatrix(4,4))

    def test_NumpyToScalar(self):
        """Implemented through automatic iterator """
        x = pg.RVector(2)
        x3 = pg.R3Vector(2)
        w = pg.RVector()

        x += np.float32(1.0)
        np.testing.assert_equal(sum(x + 1.0), 4.0)
        np.testing.assert_equal(sum(x + np.float32(1)), 4.0)
        np.testing.assert_equal(sum(x + np.float64(1)), 4.0)
        np.testing.assert_equal(sum(x - 1.0), 0.0)
        np.testing.assert_equal(sum(x - np.float32(1)), 0.0)
        np.testing.assert_equal(sum(x - np.float64(1)), 0.0)
        
        # HarmonicModelling(size_t nh, const RVector & tvec);
        pg.HarmonicModelling(np.int32(1), x);
        pg.HarmonicModelling(np.uint32(1), x);
        pg.HarmonicModelling(np.int64(1), x);
        pg.HarmonicModelling(np.uint64(1), x);

        pg.PolynomialModelling(1, np.int32(1), x3, x);
        pg.PolynomialModelling(1, np.int64(1), x3, x);
        pg.PolynomialModelling(1, np.uint32(1), x3, x);
        pg.PolynomialModelling(1, np.uint64(1), x3, x);

        x = pg.Pos(0.0, 0.0, 0.0)
        x += np.float32(1)

        np.testing.assert_equal(x, pg.Pos(1.0, 1.0, 1.0))
        np.testing.assert_equal(x -1 , pg.Pos(0.0, 0.0, 0.0))
        np.testing.assert_equal(x - np.float32(1), pg.Pos(0.0, 0.0, 0.0))
        np.testing.assert_equal(x - np.float64(1), pg.Pos(0.0, 0.0, 0.0))
        

if __name__ == '__main__':
    pg.setDeepDebug(0)
    test = TestRVectorMethods()
    
    #test.test_IndexArrayToNumpy()
    #test.test_NumpyToIVector()
    #test.test_NumpyToScalar()
    #exit()
    # test.test_BVectorToNumpy()
    # test.test_NumpyToIVector()
    # test.test_NumpyToRVector()
    # exit()


    unittest.main()
