
(defun get-arr (x n)
  (let ((arr (make-array (floor (expt x (/ 1 n))))))
    (dotimes (i (length arr) arr)
      (setf (aref arr i) (expt (- (length arr) i) n)))))

(defun ansie (x k n arr acc macc)
  (if (>= 0 x)
      (when (= x 0)
        (push acc macc))
      (do ((i k (1+ i))
           (ans nil))
          ((>= i (length arr)) macc)
          (let* ((x (- x (aref arr i))))
            (ansie x 
                   (max (1+ i) (- (length arr) (floor (expt x (/ 1 n)))))
                   n
                   arr
                   (cons (aref arr i) acc)
                   macc)))))

(defun get-ans (x n)
  (let ((arr (get-arr x n))
        (ans nil))
    (labels ((rec (x k acc)
               (if (>= 0 x)
                   (when (= x 0)
                     (push acc ans))
                   (do* ((i k (1+ i)))
                     ((>= i (length arr)))
                     (let ((x (- x (aref arr i))))
                       (rec x 
                            (max (1+ i)
                                 (- (length arr) (floor (expt x (/ 1 n)))))
                            (cons (aref arr i) acc)))))))
      (rec x 0 nil))
    ans))

(ansie 100 0 2 #(100 81 64 49 36 25 16 9 4 1) () ())
(ansie 10 0 2 #(9 4 1) ())

(get-ans 100 2)
(get-arr 100 2)
