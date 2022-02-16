(defun print-vec (n)
  (dotimes (i (length n) (terpri)) (format t "~A " (aref n i))))

(defun partition (arr l h)
  (do ((first-high l)
       (i l (1+ i)))
      ((>= i h) (progn (rotatef (aref arr h) (aref arr first-high))
                       (print-vec arr)
                       first-high))
      (when (> (aref arr h) (aref arr i))
        (rotatef (aref arr first-high) (aref arr i))
        (incf first-high))))

(defun quicksort (arr)
  (labels ((rec (l h)
             (if (> h l)
                 (let ((p (partition arr l h)))
                   (rec l (1- p))
                   (rec (1+ p) h))
                 arr)))
    (rec 0 (1- (length arr)))))

(let* ((n (read))
       (arr (make-array n :element-type 'fixnum)))
  (dotimes (i n (quicksort arr))
    (setf (aref arr i) (read))))
