(declaim (optimize (safety 0) (debug 0) (speed 3)))

(defun sieve (m n)
  (declare (fixnum m n))
  (do ((a (make-hash-table :size (- (1+ n) m) :test #'eq))
       (i 2 (1+ i)))
      ((> i (sqrt n))
       (dotimes (i (- (1+ n) m))
         (unless (gethash (+ m i) a)
           (format t "~A~%" (+ m i)))))
      (declare (fixnum i))
      (do ((j (max (* i (floor m i)) (expt i 2)) (+ j i)))
          ((> j n))
          (declare (fixnum j))
          (when (>= j m)
            (setf (gethash j a) t)))))

(defun main ()
  (dotimes (_ (read))
    (sieve (max (read) 2) (read))
    (terpri)))

(main)

(time (sieve 500000000 501000000))
(eq 1 1)
(+ 1 2)

(sieve 2 101)

