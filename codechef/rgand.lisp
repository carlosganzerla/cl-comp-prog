(defun slow-ans (l r)
  (do ((s 0)
       (i l (1+ i)))
      ((> i r) s)
      (do ((j l (1+ j))
           (x l (logand x j)))
          ((> j i) (incf s x)))))

(bit-and 5 6)

(slow-ans 4 10)
(slow-ans 13 18)

(logand 10 11)

(defun to-bits (integer)
  (let ((i integer)
        (bits (make-array (integer-length integer) 
                          :element-type 'bit)))
    (dotimes (j (length bits) bits)
      (setf (aref bits (- (length bits) j 1)) (logand i 1))
      (setf i (ash i -1)))) )

(defun from-bits (vector)
  (let ((n 0))
    (dotimes (i (length vector) n)
      (incf n (* (bit vector i) (expt 2 (- (length vector) i 1)) )))))


(defun fast-ans (l)
  (do* ((vec (to-bits l))
        (i 0 (1+ i))
        (occ (make-array (length vec))))
    ((>= i (length vec)) occ)
    (let ((n (expt 2 i)))
      (setf (aref occ (- (length vec) 1 i)) (- n (mod l n))))))


(fast-ans 13)

(defun fast-ans (l)
  (do ((i 0 (1+ i))
       (nums nil))
      ((>= i (integer-length l)) nums)
      (let* ((e (expt 2 (1+ i)))
             (c (- e (mod l e)))
             (p (logxor l (mod l (expt 2 i)))))
        (format t "~A ~A ~A~%" e c p)
        (dotimes (_ (- c (length nums)))
          (push p nums)))))

(fast-ans 4)
(fast-ans 1)
(fast-ans 13)

(logxor 13 1)

