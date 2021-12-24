(defun fac (n)
  (labels ((rec (n acc)
             (if (> n 0)
                 (rec (1- n) (* n acc))
                 acc)))
    (rec n 1)))

(defun comb (n k)
  (/ (fac n) (* (fac k) (fac (- n k)))))

(defun get-sub-vec (vec k)
  (do ((i 0 (1+ i))
       (sum 0))
      ((or (>= i (length vec)) (> (aref vec i)
                                  (aref vec (1- k))))

       (subseq vec 0 i))))

(defun get-ans (vec k)
  (let ((vec (get-sub-vec (sort vec #'<) k)))
    (do ((i 0 (1+ i))
         (init (aref vec 0)))
        ((>= i (length vec)) (comb (length vec) k))
        (when (and (= (aref vec i) (aref vec (1- k))) (> (aref vec i) init))
          (return (comb (- (length vec) i) (- k i)))))))

(defun read-vec (n)
  (let ((vec (make-array n :element-type 'fixnum)))
    (dotimes (i n vec)
      (setf (aref vec i) (read)))))

(defun main ()
  (dotimes (_ (read))
    (let ((n (read)) (k (read)))
      (format t "~A~%" (get-ans (read-vec n) k)))))

(main)
