(defun get-arr (x n)
  (let ((arr (make-array (floor (expt x (/ 1 n))))))
    (dotimes (i (length arr) arr)
      (setf (aref arr i) (expt (- (length arr) i) n)))))


(defun get-ans (x n)
  (let ((arr (get-arr x n))
        (ans nil))
    (labels ((rec (x k acc)
               (if (>= 0 x)
                   (when (= x 0)
                     (push acc ans))
                   (do ((i k (1+ i)))
                       ((>= i (length arr)))
                       (let ((x (- x (aref arr i))))
                         (rec x 
                              (max (1+ i)
                                   (- (length arr) (floor (expt x (/ 1 n)))))
                              (cons (aref arr i) acc)))))))
      (rec x 0 nil))
    ans))

(format t "~A" (length (get-ans (read) (read))))
